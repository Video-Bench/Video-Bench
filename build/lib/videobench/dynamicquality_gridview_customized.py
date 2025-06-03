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
    model_scores = {}
    dataset = Video_Dataset(cur_full_info_path)
    
    usrmessages ={'temporal_consistency':'temporal consistency', 'motion_effects':'motion effects'}
    dim = usrmessages[dimension]

    l1 = list(range(0, len(dataset)))
    for i in l1:
        
        logger.info(f'Processing video {i}...')
        data = dataset[i]
        frames = data['grid_frames']
        prompten = data['prompt']
        results[i] = {}
        results[i]['prompt_en'] = prompten
        available_models = list(data['frames'].keys())
        models_to_process = models if models else available_models

        # 构建包含所有模型帧的消息
        for modelname in models_to_process:

            if modelname not in model_scores:
                model_scores[modelname] = {'total_score': 0, 'count': 0}

            try:
                messages = [
                    {
                        "role": "system",
                        "content": prompt
                    },
                    {
                        "role": "user", 
                        "content": [
                            "The following images are concatenated by the key frames of the video.And one of the following images arranges 4 key frames per second from a video in a 1*4 grid view.\n" ,
                            "Please associate the images in time order to help you watch the whole video.\n",
                            *map(lambda x: {"type": "image_url", 
                                "image_url": {"url": f'data:image/jpg;base64,{x}', "detail": "low"}},frames[modelname]),    
                            "Find the issues of the video in {} and then evaluate the {} of the video.\n".format(dim,dim),                       
                            "Assuming there are a video scoring 'x',provide your analysis and explanation in the output format as follows:\n"
                            "- video: x ,because ..."
                        ]
                    }
                ]

                response = call_api(client, messages, MODEL)
                logger.info(f'>>>>>>>This is the {i} round >>>>>>evaluation results>>>>>>:\n{response}\n')

                match = re.search(r':\s*(\d+)', response)
                if match:
                    video_score = int(match.group(1))
                else:
                    video_score = 'Error'
                results[i][modelname] = video_score

                 # 将最终评分累加到模型总分中
                model_scores[modelname]['total_score'] += video_score
                model_scores[modelname]['count'] += 1
                
            except Exception as e:
                logger.error(f'Error evaluating model {modelname}: {str(e)}')
                results[i][modelname] = 'Error'

    average_scores = {model: model_scores[model]['total_score'] / model_scores[model]['count']
                  for model in model_scores if model_scores[model]['count'] > 0}

    return {
        'score': results,
        'average_scores': average_scores  # 每个模型的平均分
    }