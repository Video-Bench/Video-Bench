import os
import re
from openai import OpenAI
import openai
from .utils import Video_Dataset
import json
import logging
from tenacity import retry, stop_after_attempt, wait_random_exponential

@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def call_api(client, messages, model):
    """调用 OpenAI API 的函数，包含重试机制"""
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content

def extract_scores_from_result(response):
    because_matches = re.finditer(r'because', response)
    scores = []

    for match in because_matches:
        start_idx = match.start()  # 获取 'because' 起始位置

        # 在 'because' 前面查找最近的数字
        preceding_content = response[:start_idx]
        preceding_number_match = re.search(r'\d+', preceding_content[::-1])  # 反转字符串查找第一个数字

        if preceding_number_match:
            number = preceding_number_match.group()[::-1]  # 提取并翻转数字
            scores.append(int(number))  # 转为整数

    return scores

def eval(config, prompt, dimension, cur_full_info_path,models):
    """
    Evaluate videos using OpenAI API
    Args:
        config: configuration dictionary
        prompt: prompt template
        dimension: evaluation dimension name
    Returns:
        dict: containing evaluation scores
    """
    # 设置日志
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler(config[f'log_path_{dimension}'])
    formatter = logging.Formatter('%(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    client = OpenAI(
        api_key = config['GPT4o_API_KEY'],
        base_url = config['GPT4o_BASE_URL']
    )
    MODEL = "gpt-4o-2024-08-06"

    results = {}
    dataset = Video_Dataset(cur_full_info_path)
    
    l1 = list(range(0, len(dataset)))
    model_scores = {model: {"total_score": 0, "count": 0} for model in models}

    for i in l1:
        try:
            data = dataset[i]
            frames = data['frames']
            prompten = data['prompt']

            results[i] = {}
            results[i]['prompt_en'] = data['prompt']
            
            model_names = list(frames.keys())
            # 构建包含所有模型帧的消息
            model_frames_content = []
            for model_name, model_frames in frames.items():
                model_frames_content.extend([
                    f"\n{len(model_frames)} frames from {model_name}\n",
                    *map(lambda x: {"type": "image_url", 
                                  "image_url": {"url": f'data:image/jpg;base64,{x}', "detail": "low"}}, 
                         model_frames)
                ])

            messages = [
                {
                    "role": "system",
                    "content": prompt
                },
                {
                    "role": "user", 
                    "content": [
                        f"These are the frames from the video. The prompt is '{prompten}'.",
                        *model_frames_content
                    ]
                }
            ]

            response = call_api(client, messages, MODEL)
            logger.info(f'>>>>>>>This is the {i} round >>>>>>evaluation results>>>>>>:\n{response}\n')

            scores = extract_scores_from_result(response)

            # Step 4: 将数字与 model_name 对应
            model_scores_dict = dict(zip(model_names, scores))
            filtered_scores = {name: model_scores_dict[name] for name in models if name in model_scores_dict}
            results[i].update(filtered_scores)
            
            # 更新模型的总分和计数
            for model_name, score in filtered_scores.items():
                model_scores[model_name]["total_score"] += score
                model_scores[model_name]["count"] += 1
            
        except Exception as e:
            logger.error(f'Error processing video {i}: {str(e)}')
            results[str(i)] = f'Error: {str(e)}'

    average_scores = {model: model_scores[model]['total_score'] / model_scores[model]['count']
                  for model in model_scores if model_scores[model]['count'] > 0}

    return {
        'score': results,
        'average_scores': average_scores  # 每个模型的平均分
    }