#!/usr/bin/env python
import os
import sys
import json
import argparse
from datetime import datetime
from videobench import VideoBench

def parse_args():
    CUR_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    parser = argparse.ArgumentParser(
        description='Video-Bench - Human Preference Aligned Video Generation Benchmark'
    )
    
    parser.add_argument(
        "--output_path",
        type=str,
        default='./evaluation_results/',
        help="output path to save the evaluation results"
    )
    
    parser.add_argument(
        "--config_path",
        type=str,
        default='./config.json',
        help="path to the config file"
    )
    
    parser.add_argument(
        "--log_path",
        type=str,
        default='./logs/',
        help="log path to save the logs"
    )
    
    parser.add_argument(
        "--videos_path",
        type=str,
        required=True,
        help="folder that contains the sampled videos"
    )
    
    parser.add_argument(
        "--dimension",
        nargs='+',
        required=True,
        help="list of evaluation dimensions, usage: --dimension <dim_1> <dim_2>"
    )
    
    parser.add_argument(
        "--mode",
        type=str,
        choices=['standard', 'custom_static', 'custom_nonstatic'],
        default='standard',
        help="evaluation mode to use: standard mode or custom input mode"
    )

    
    parser.add_argument(
        "--full_json_dir",
        type=str,
        default=os.path.join(CUR_DIR, "videobench", "VideoBench_full.json"),
        help="path to save the json file that contains the prompt and dimension information"
    )

    parser.add_argument(
        "--prompt",
        type=str,
        default="None",
        help="""Specify the input prompt
        If not specified, filenames will be used as input prompts
        * Mutually exclusive to --prompt_file.
        ** This option must be used with --mode=custom_input flag
        """
    )

    parser.add_argument(
        "--prompt_file",
        type=str,
        default=None,
        help="""Specify the path of the file that contains prompt lists
        If not specified, filenames will be used as input prompts
        * Mutually exclusive to --prompt.
        ** This option must be used with --mode=custom_input flag
        """
    )
    parser.add_argument(
        "--models",
        nargs='+',
        default=[],
        help="list of model names to evaluate"
    )
    args = parser.parse_args()
    return parser.parse_args()

def main():
    args = parse_args()
    os.makedirs(args.log_path, exist_ok=True)

    # 处理 prompt
    prompt_list = {}
    if args.prompt_file and os.path.exists(args.prompt_file):
        # 从文件加载提示词映射
        with open(args.prompt_file, 'r') as f:
            prompt_list = json.load(f)
            if not isinstance(prompt_list, dict):
                raise ValueError("Prompt file must contain a dictionary mapping extracted prompts to actual prompts")
    elif args.prompt != "None":
        # 使用单个提示词
        prompt_list = args.prompt

    bench_runner = VideoBench(args.full_json_dir, args.output_path, args.config_path)
    dimension_str = args.dimension[0]

    try:
        bench_runner.evaluate(
            videos_path=args.videos_path,
            name=f'results_{dimension_str}',
            dimension_list=args.dimension,
            mode=args.mode,
            models=args.models,
            prompt_list=prompt_list
        )
        print(f"\nEvaluation completed successfully!")
        
    except Exception as e:
        print(f"\nError during evaluation: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main() 