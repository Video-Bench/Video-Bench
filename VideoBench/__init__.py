import os
import importlib
from pathlib import Path
from itertools import chain
from .utils import save_json, load_json, get_prompt_from_filename

class VideoBench(object):
    def __init__(self, full_info_dir, output_path, config_path):
        """
        Initialize VBench evaluator
        
        Args:
            full_info_dir (str): Path to the full info JSON file
            output_path (str): Directory to save evaluation results
            config_path (str): Path to configuration file
        """
        self.full_info_dir = full_info_dir  
        self.output_path = output_path
        self.config_path = config_path
        self.config = load_json(config_path)
        os.makedirs(self.output_path, exist_ok=True)

    def build_full_dimension_list(self):
        """Return list of all available evaluation dimensions"""
        return [
           "aesthetic_quality", "imaging_quality", "temporal_consistency", "motion_effects", 
           "color", "object_class", "scene", "action", "video-text consistency"
        ]
    
    def check_dimension_requires_extra_info(self, dimension_list):
        """Check if any dimension requires extra information"""
        VideoTextConsistency_dimensions = ['color', 'object_class', 'scene', 'action', 'video-text consistency']
        for dim in dimension_list:
            if dim in VideoTextConsistency_dimensions:
                return True
        return False
    
    def build_full_info_json(self, videos_path, name, dimension_list, prompt_list=[], special_str='', verbose=True, mode='standard', models=[], **kwargs):
        """Build full info JSON file containing video paths and prompts"""
        cur_full_info_list = []
        
        # 定义维度映射关系
        dimension_mapping = {
            'aesthetic_quality': 'video-text consistency',
            'imaging_quality': 'video-text consistency',
            'temporal_consistency': 'action',
            'motion_effects': 'action',
            'video-text consistency': 'video-text consistency',
            'action': 'action',
            'color': 'color',
            'object_class': 'object_class',
            'scene': 'scene'
        }
        
        if mode == 'custom_nonstatic':
            self.check_dimension_requires_extra_info(dimension_list)
            actual_dimensions = set(dimension_mapping[dim] for dim in dimension_list)
            
            # 处理 prompt_list
            prompts_to_process = []
            if isinstance(prompt_list, str):
                prompts_to_process.append(prompt_list)
            elif isinstance(prompt_list, dict):
                prompts_to_process.extend(prompt_list.values())
            else:
                prompts_to_process.extend(prompt_list)
            print(f"Prompts to process: {prompts_to_process}")
            for prompt in prompts_to_process:
                videos_by_prompt = {}
                
                for actual_dim in actual_dimensions:
                    dimension_path = os.path.join(videos_path, actual_dim)
                    if os.path.exists(dimension_path):
                        # 只处理指定的模型
                        available_models = [name for name in os.listdir(dimension_path) if os.path.isdir(os.path.join(dimension_path, name))]
                        for model_name in available_models:
                            model_path = os.path.join(dimension_path, model_name)
                            if os.path.isdir(model_path):
                                for video_name in os.listdir(model_path):
                                    if Path(video_name).suffix.lower() in ['.mp4', '.gif', '.jpg', '.png']:
                                        video_path = os.path.join(dimension_path, model_name, video_name)
                                        extracted_prompt = get_prompt_from_filename(video_name)
                                        if extracted_prompt == prompt:
                                            if prompt not in videos_by_prompt:
                                                videos_by_prompt[prompt] = {}
                                            videos_by_prompt[prompt][model_name] = video_path.replace("\\", "/")
                
                if videos_by_prompt:
                    for prompt_key, videos in videos_by_prompt.items():
                        cur_full_info_list.append({
                            "prompt_en": prompt_key,
                            "dimension": dimension_list,
                            "videos": videos
                        })
        
        elif mode == 'custom_static':
            if not models:
                raise ValueError("The 'models' parameter cannot be empty. Please specify at least one model to evaluate.")

            # 获取实际的数据目录
            actual_dimensions = set(dimension_mapping[dim] for dim in dimension_list)
            
            # 获取 videos_path 下的所有 model_name
            model_names = [d for d in os.listdir(videos_path) if os.path.isdir(os.path.join(videos_path, d))]
            
            # 从 full_info_dir 中加载所有 prompts
            full_info_list = load_json(self.full_info_dir)
            all_prompts = [item['prompt'] for item in full_info_list]
            
            # 处理 prompt_list
            prompts_to_process = []
            if isinstance(prompt_list, str):
                prompts_to_process.append(prompt_list)
            elif isinstance(prompt_list, dict):
                prompts_to_process.extend(prompt_list.values())
            else:
                prompts_to_process.extend(prompt_list)
            
            # 对每个 prompt 进行处理
            for prompt in prompts_to_process:
                # 在 full_info_list 中找到最相似的 prompt
                from difflib import SequenceMatcher
                def similar(a, b):
                    return SequenceMatcher(None, a, b).ratio()
                
                prompt_similar = max(all_prompts, key=lambda x: similar(x, prompt))
                print(f"Most similar prompt to '{prompt}': {prompt_similar}")
                
                videos_dict = {}
                # 遍历每个维度目录
                for actual_dim in actual_dimensions:
                    dimension_path = os.path.join(videos_path, actual_dim)
                    if os.path.exists(dimension_path):
                        # 遍历每个模型目录
                        available_models = [name for name in os.listdir(dimension_path) if os.path.isdir(os.path.join(dimension_path, name))]
                        for model_name in available_models:
                            model_path = os.path.join(dimension_path, model_name)
                            
                            # 检查是否是有效目录
                            if not os.path.isdir(model_path):
                                print(f"Warning: Model directory {model_path} not found, skipping...")
                                continue

                            # 获取模型目录中的所有视频文件
                            video_files = [f for f in os.listdir(model_path) if Path(f).suffix.lower() in ['.mp4', '.gif', '.jpg', '.png']]

                            # 优先检查完全匹配的视频
                            exact_matches = [f for f in video_files if prompt in get_prompt_from_filename(f)]
                            if exact_matches:
                                # 如果找到完全匹配的视频，检查模型是否在 models 中
                                if model_name in models:
                                    video_path = os.path.join(dimension_path, model_name, exact_matches[0])
                                    videos_dict[model_name] = os.path.abspath(video_path).replace("\\", "/")
                                # 跳过不在 models 中的模型
                                continue

                            # 如果没有完全匹配的视频，查找与 prompt_similar 相似的视频
                            similar_matches = [f for f in video_files if prompt_similar in get_prompt_from_filename(f)]
                            if similar_matches:
                                video_path = os.path.join(dimension_path, model_name, similar_matches[0])
                                videos_dict[model_name] = os.path.abspath(video_path).replace("\\", "/")

                
                if videos_dict:
                    cur_full_info_list.append({
                        "prompt_en": prompt,
                        "dimension": dimension_list,
                        "videos": videos_dict
                    })
        
        else:
            # Standard mode using benchmark data
            full_info_list = load_json(self.full_info_dir)
            
            for prompt_dict in full_info_list:
                # 检查是否有任何请求的维度在这个提示词的维度列表中
                if any(dim in dimension_list for dim in prompt_dict["dimension"]):
                    prompt = prompt_dict['prompt']
                    videos_dict = {}
                    
                    # 获取实际的数据目录
                    actual_dimensions = set(dimension_mapping[dim] for dim in dimension_list 
                                         if dim in prompt_dict["dimension"])
                    
                    # 遍历每个实际维度目录
                    for actual_dim in actual_dimensions:
                        dimension_path = os.path.join(videos_path, actual_dim)
                        if os.path.exists(dimension_path):
                            # 处理当前目录下的模型
                            available_models = [name for name in os.listdir(dimension_path) if os.path.isdir(os.path.join(dimension_path, name))]
                            # 初始化后缀分组
                            suffix_videos = {idx: {} for idx in range(3)}  # 用于存储 _0, _1, _2 的分组
                            no_suffix_videos = {}  # 用于存储没有后缀的视频
                            for model_name in available_models:
                                model_path = os.path.join(dimension_path, model_name)
                                if os.path.isdir(model_path):
                                    # 首先检查无后缀的视频
                                    no_suffix_video_name = f"{prompt}.mp4"
                                    no_suffix_video_path = os.path.join(dimension_path, model_name, no_suffix_video_name)
                                    
                                    if os.path.exists(no_suffix_video_path):
                                        no_suffix_videos[model_name] = no_suffix_video_path.replace("\\", "/")
                                        # if verbose:
                                        #     print(f'Successfully found video without suffix: {no_suffix_video_path}')
                                    else:
                                        # 检查带后缀的视频
                                        for idx in range(3):
                                            video_name = f"{prompt}_{idx}.mp4"
                                            video_path = os.path.join(dimension_path, model_name, video_name)
                                            
                                            if os.path.exists(video_path):
                                                # 将视频路径存入对应的后缀分组
                                                suffix_videos[idx][model_name] = video_path.replace("\\", "/")
                                                # if verbose:
                                                #     print(f'Successfully found video: {video_path}')
                                            elif verbose:
                                                print(f'Error!!! Required video not found: {video_path}')
                            
                            # 如果存在无后缀的视频，优先添加到 cur_full_info_list
                            if no_suffix_videos:
                                cur_full_info_list.append({
                                    "prompt_en": prompt,
                                    "dimension": dimension_list,
                                    "videos": no_suffix_videos
                                })
                            
                            # 将每个后缀的分组信息添加到 cur_full_info_list
                            for idx, videos_dict in suffix_videos.items():
                                if videos_dict:  # 确保分组中有视频
                                    cur_full_info_list.append({
                                        "prompt_en": prompt,
                                        "dimension": dimension_list,
                                        "videos": videos_dict
                                    })

        cur_full_info_path = os.path.join(self.output_path, name+'_full_info.json')
        save_json(cur_full_info_list, cur_full_info_path)
        print(f'Evaluation meta data saved to {cur_full_info_path}')
        return cur_full_info_path

    def evaluate_dimension(self, dimension, videos_path, name, dimension_list, prompt_list, mode, models=[], **kwargs):
        """Evaluate a single dimension by importing and running its module"""
        # 只传入当前维度
        cur_dimension_list = [dimension]
        
        cur_full_info_path = self.build_full_info_json(
            videos_path=videos_path,
            name=name,
            dimension_list=cur_dimension_list,
            prompt_list=prompt_list,
            mode=mode,
            models=models,
            **kwargs
        )

        try:
            VideoTextAlignment_dimensions = ['color', 'object_class', 'scene', 'action', 'video-text consistency']
            static_dimensions = ['aesthetic_quality', 'imaging_quality']
            dynamic_dimensions = ['temporal_consistency', 'motion_effects']

            from .prompt_dict import prompt

            if dimension in VideoTextAlignment_dimensions:
                from .VideoTextAlignment import eval
                results = eval(self.config, prompt[dimension], dimension, cur_full_info_path,models)
            
            elif dimension in static_dimensions:
                if mode == 'custom_static':
                    from .staticquality_customized import eval
                    results = eval(self.config, prompt[dimension], dimension, cur_full_info_path,models)
                else:
                    from .staticquality import eval
                    results = eval(self.config, prompt[dimension], dimension, cur_full_info_path,models)
            
            elif dimension in dynamic_dimensions:
                if mode == 'custom_nonstatic':
                    # 自定义模式使用 gridview 的评估函数
                    from .dynamicquality_gridview_customized import eval
                    results = eval(self.config, prompt[dimension], dimension, cur_full_info_path,models)
                else:
                    # 标准模式使用原来的评估函数
                    from .dynamicquality import eval
                    results = eval(self.config, prompt[dimension], dimension, cur_full_info_path,models)
            
            else:
                raise ValueError(f"Unknown dimension: {dimension}")
            
            return results
            
        except Exception as e:
            print(f"Error evaluating {dimension}: {e}")
            return {'error': str(e)}

    def evaluate(self, videos_path, name, dimension_list=None, mode='standard', models=[], prompt_list=[], **kwargs):
        """
        Run evaluation on specified dimensions
        
        Args:
            videos_path (str): Path to video files
            name (str): Name for this evaluation run
            dimension_list (list): List of dimensions to evaluate
            mode (str): Evaluation mode ('standard', 'custom_static', or 'custom_nonstatic')
            models (list): List of model names to evaluate, if empty will use all available models
            prompt_list (dict/str): Dictionary mapping video paths to prompts or single prompt string
            **kwargs: Additional arguments
        """
        # Use default dimension list if none provided
        if dimension_list is None:
            dimension_list = self.build_full_dimension_list()
            print(f'Using default dimension list: {dimension_list}')
        
        # Evaluate each dimension
        results = {}
        for dimension in dimension_list:
            print(f"Evaluating {dimension}...")
            dimension_results = self.evaluate_dimension(
                dimension=dimension,
                videos_path=videos_path,
                name=name,
                dimension_list=dimension_list,
                prompt_list=prompt_list,
                mode=mode,
                models=models,
                **kwargs
            )

            # 为每个维度创建输出目录
            dimension_output_dir = os.path.join(self.output_path, dimension)
            os.makedirs(dimension_output_dir, exist_ok=True)
            
            # 保存结果
            VideoTextAlignment_dimensions = ['color', 'object_class', 'scene', 'action', 'video-text consistency']
            if dimension in VideoTextAlignment_dimensions:
                save_json(dimension_results['history'], os.path.join(dimension_output_dir, f'{name}_history_results.json'))
            
                combined_scores = {
                "average_scores": dimension_results.get("average_scores", {}),
                "scores": dimension_results.get("score", {})
                }
                save_json(combined_scores, os.path.join(dimension_output_dir, f'{name}_score_results.json'))
            else:
                combined_scores = {
                "average_scores": dimension_results.get("average_scores", {}),
                "scores": dimension_results.get("score", {})
                }
                save_json(combined_scores, os.path.join(dimension_output_dir, f'{name}_score_results.json'))

            results[dimension] = dimension_results
        
        return results
