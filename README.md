# Video-Bench: Human Preference Aligned Video Generation Benchmark


Video-Bench is a benchmark tool designed to systematically leverage MLLMs across all dimensions relevant to video generation assessment in generative models. By incorporating few-shot scoring and chain-of-query techniques, Video-Bench provides a structured, scalable approach to generating video evaluation.

<a href="https://arxiv.org/pdf/2504.04907" alt="paper"><img src="https://img.shields.io/badge/ArXiv-2504.04907-FAA41F.svg?style=flat" /></a>
<a href="https://videobench.github.io/VideoBench-project/" alt="demo"><img src="https://img.shields.io/badge/Demo-VideoBench-orange" /></a> 
<a href="https://mp.weixin.qq.com/s/CtbyZhg4HvYnPocBLfnTrw" alt="blog"><img src="https://img.shields.io/badge/Blog-SharingPlatform-green" /></a> 
<a href="https://zhuanlan.zhihu.com/p/xxx" alt="zhihu"><img src="https://img.shields.io/badge/Zhihu-知乎-blue" /></a> 
<a href="https://www.youtube.com/watch?v=xxx" alt="video"><img src="https://img.shields.io/badge/Video-YouTube-purple" /></a>
<a href="https://xxx" alt="twitter"><img src="https://img.shields.io/badge/Post-Twitter-1DA1F2" /></a>

 
![Multi-Modal](https://img.shields.io/badge/Task-Vision--Perception-red) 
![Foundation-Model](https://img.shields.io/badge/Task-Video--Understanding-red) 
![Foundation-Model](https://img.shields.io/badge/Task-Video--Generation-red) 
![Video-Understanding](https://img.shields.io/badge/Task-Video--Evaluation-red) 
![Video-Generation](https://img.shields.io/badge/Task-Video--Benchmark-red) 
![Video-Recommendation](https://img.shields.io/badge/Task-MLLM--Application-red) 
![Video-Recommendation](https://img.shields.io/badge/Task-Human--Preference--Learning-red) 
![Video-Recommendation](https://img.shields.io/badge/Dataset-Human--Annotation-red) 

[⭐Overview](#Overview) |
[📒Leaderboard](#Leaderboard) |
[🤗HumanAlignment](#HumanAlignment) |
[🛠️Installation](#Installation) |
[🗃️Preparation](#Preparation) |
[⚡Instructions](#Instructions) |
[🚀Usage](#Usage) |
[📭Citation](#Citation) |
[📝Literature](#Literature) 

## Contents

- [Overview](#overview)
- [Leaderboard](#leaderboard)
- [Installation](#installation)
- [HumanAlignment](#humanalignment)
- [Installation](#installation)
   - [Installation Requirements](#installation-requirements)
   - [Pip Installation](#pip-installation)
   - [Download From Huggingface](#download-from-huggingface)
- [Preparation](#preparation)
- [Instruction](#instruction)
- [Usage](#usage)
   - [Standard Mode](#standard-mode)
   - [Custom Mode](#custom-mode)
   - [Videos and Annotations](#videos-and-annotations)
- [Citation](#Citation)
- [Literature](#literature)

# Overview

<div align=center><img src="https://github.com/Video-Bench/Video-Bench/blob/main/figures/videobench.png"/></div>

# Leaderboard

| Model            | Imaging Quality | Aesthetic Quality | Temporal Consist. | Motion Effects | Avg Rank | Video-text Consist. | Object-class Consist. | Color Consist. | Action Consist. | Scene Consist. | Avg Rank | Overall Avg Rank |
|------------------|-----------------|-------------------|--------------------|----------------|----------|----------------------|-----------------------|----------------|-----------------|----------------|----------|------------------|
| Cogvideox [57]   | 3.87            | 3.84              | 4.14               | 3.55           | 3.00     | **4.62**             | 2.81                 | **2.92**        | 2.81            | **2.93**       | **1.60**  | 2.22             |
| Gen3 [42]        | **4.66**        | **4.44**          | **4.74**           | **3.99**       | **1.00** | 4.38                 | 2.81                 | 2.87            | 2.59            | **2.93**       | 2.40      | **1.78**         |
| Kling [24]       | 4.26            | 3.82              | 4.38               | 3.11           | 2.75     | 4.07                 | 2.70                 | 2.81            | 2.50            | 2.82           | 4.60      | 3.78             |
| VideoCrafter2 [5] | 4.08            | 3.85              | 3.69               | 2.81           | 3.75     | 4.18                 | **2.85**             | 2.90            | 2.53            | 2.78           | 2.80      | 3.22             |
| LaVie [52]       | 3.00            | 2.94              | 3.00               | 2.43           | 7.00     | 3.71                 | 2.82                 | 2.81            | 2.45            | 2.63           | 5.00      | 5.88             |
| PiKa-Beta [38]   | 3.78            | 3.76              | 3.40               | 2.59           | 5.50     | 3.78                 | 2.51                 | 2.52            | 2.25            | 2.60           | 6.80      | 6.22             |
| Show-1 [60]      | 3.30            | 3.28              | 3.90               | 2.90           | 5.00     | 4.21                 | 2.82                 | 2.79            | 2.53            | 2.72           | 3.80      | 4.33             |

**Notes**:
- Higher scores indicate better performance.
- The best score in each dimension is highlighted in **bold**.

# HumanAlignment

| Metrics     | Benchmark      | Imaging Quality | Aesthetic Quality | Temporal Consist. | Motion Effects | Video-text Consist. |  Action Consist. |Object-class Consist. | Color Consist. | Scene Consist. |
|-------------|----------------|------------------|--------------------|--------------------|----------------|----------------------|-----------------------|----------------|-----------------|----------------|
| MUSIQ [21]  | VBench [19]    | 0.363           | -                  | -                  | -              | -                    | -                     | -              | -               | -              |
| LAION       | VBench [19]    | -               | 0.446              | -                  | -              | -                    | -                     | -              | -               | -              |
| CLIP [40]   | VBench [19]    | -               | -                  | 0.260              | -              | -                    | -                     | -              | -               | -              |
| RAFT [48]   | VBench [19]    | -               | -                  | -                  | 0.329          | -                    | -                     | -              | -               | -              |
| Amt [28]    | VBench [19]    | -               | -                  | -                  | 0.329          | -                    | -                     | -              | -               | -              |
| ViCLIP [53] | VBench [19]    | -               | -                  | -                  | -              | 0.445                | -                     | -              | -               | -              |
| UMT [27]    | VBench [19]    | -               | -                  | -                  | -              | -                    | 0.411                 | -              | -               | -              |
| GRiT [54]   | VBench [19]    | -               | -                  | -                  | -              | -                    | -                     | 0.469          | 0.545           | -              |
| Tag2Text [16]| VBench [19]   | -               | -                  | -                  | -              | -                    | -                     | -              | -               | 0.422            |
| ComBench [46]| ComBench [46] | -               | -                  | -                  | -              | 0.633                | 0.633                 | 0.611          | 0.696           | 0.631           |
| **Video-Bench**    | **Video-Bench**       | **0.733**       | **0.702**          | **0.402**          | **0.514**      | **0.732**            | **0.718**             | **0.735**      | **0.750**       | **0.733**      |

**Notes**:
- Higher scores indicate better performance.
- The best score in each dimension is highlighted in **bold**.


# Installation

## Installation Requirements
- Python >= 3.8
- OpenAI API access
   Update your OpenAI API keys in `config.json`:
   ````json
   {
       "GPT4o_API_KEY": "your-api-key",
       "GPT4o_BASE_URL": "your-base-url",
       "GPT4o_mini_API_KEY": "your-mini-api-key",
       "GPT4o_mini_BASE_URL": "your-mini-base-url"
   }
   ````

## Pip Installation

- Install with pip
   ````bash
   pip install videobench
   ````

- Install with git clone

   ````bash
   git clone https://github.com/Video-Bench/Video-Bench.git
   cd Video-Bench
   pip install -r requirements.txt
   ````

## Download From Huggingface

   ````bash
   wget https://huggingface.co/Video-Bench/Video-Bench 
   ````
   or
   ````bash
   curl -L https://huggingface.co/Video-Bench/Video-Bench 
   ````

# Preparation
<a id="data-structure"></a>
Please organize your data according to the following [data structure](#data-structure):
```bash
# Data Structure
/Video-Bench/data/
├── color/                           # 'color' dimension videos
│   ├── cogvideox5b/
│   │   ├── A red bird_0.mp4
│   │   ├── A red bird_1.mp4
│   │   └── ...
│   ├── lavie/
│   │   ├── A red bird_0.mp4
│   │   ├── A red bird_1.mp4
│   │   └── ...
│   ├── pika/
│   │   └── ...
│   └── ...
│
├── object_class/                    # 'object_class' dimension videos
│   ├── cogvideox5b/
│   │   ├── A train_0.mp4
│   │   ├── A train_1.mp4
│   │   └── ...
│   ├── lavie/
│   │   └── ...
│   └── ...
│
├── scene/                           # 'scene' dimension videos
│   ├── cogvideox5b/
│   │   ├── Botanical garden_0.mp4
│   │   ├── Botanical garden_1.mp4
│   │   └── ...
│   └── ...
│
├── action/                          # 'action' 'temporal_consistency' 'motion_effects' dimension videos
│   ├── cogvideox5b/
│   │   ├── A person is marching_0.mp4
│   │   ├── A person is marching_1.mp4
│   │   └── ...
│   └── ...
│
└── video-text consistency/             # 'video-text consistency' 'imaging_quality' 'aesthetic_quality' dimension videos
    ├── cogvideox5b/
    │   ├── Close up of grapes on a rotating table._0.mp4
    │   └── ...
    ├── lavie/
    │   └── ...
    ├── pika/
    │   └── ...
    └── ...
```

# Instructions

Video-Bench provides a comprehensive evaluation across multiple dimensions of video generation quality. Each dimension is assessed using a specific scoring scale to ensure accurate and meaningful evaluation.

## Evaluation Dimensions

<a id="module"></a>
<a id="static-quality"></a>
<a id="dynamic-quality"></a>
<a id="video-text-alignment"></a>

| Dimension | Description | Scale | [Module](#module) |
|-----------|-------------|--------|---------|
| **[Static Quality](#static-quality)** |
| Image Quality | Evaluates technical aspects including clarity and sharpness | 1-5 | `staticquality.py` |
| Aesthetic Quality | Assesses visual appeal and artistic composition | 1-5 | `staticquality.py` |
| **[Dynamic Quality](#dynamic-quality)** |
| Temporal Consistency | Measures frame-to-frame coherence and smoothness | 1-5 | `dynamicquality.py` |
| Motion Effects | Evaluates quality of movement and dynamics | 1-5 | `dynamicquality.py` |
| **[Video-Text Alignment](#video-text-alignment)** |
| Video-Text Consistency | Overall alignment with text prompt | 1-5 | `VideoTextAlignment.py` |
| Object-Class Consistency | Accuracy of object representation | 1-3 | `VideoTextAlignment.py` |
| Color Consistency | Matching of colors with text prompt | 1-3 | `VideoTextAlignment.py` |
| Action Consistency | Accuracy of depicted actions | 1-3 | `VideoTextAlignment.py` |
| Scene Consistency | Correctness of scene environment | 1-3 | `VideoTextAlignment.py` |

# Usage

Video-Bench supports two modes: standard mode and custom input mode.
Video-Bench only supports assessments of the following dimensions: `'aesthetic_quality', 'imaging_quality','temporal_consistency', 'motion_effects','color', 'object_class', 'scene', 'action', 'video-text consistency'`

## Standard Mode
The Standard Mode assesses videos generated by various video generation models using the prompt suite defined in our `VideoBench_full.json`. 

It allows users to organize three sets of video data for the seven provided models or add three sets for other models following the [data structure](#data-structure). It also supports using only one set of video data for all models. Please ensure that the number of data sets is consistent across all models within the [data structure](#data-structure).

To evaluate videos, simply specify the models to be tested in the --models parameter. For example, if you want to evaluate videos under `modelname1` and `modelname2`, use the following commands with `--models modelname1 modelname2`

```bash
python evaluate.py \
 --dimension $DIMENSION \
 --videos_path ./data/ \
 --config_path ./config.json \
 --models modelname1 modelname2
```
or
```bash
videobench \
 --dimension $DIMENSION \
 --videos_path ./data/ \
 --config_path ./config.json \
 --models modelname1 modelname2
```

## Custom Mode
This mode allows users to evaluate videos generated from prompts that are not included in the Video-Bench prompt suite.

You can provide prompts in two ways:
1. Single prompt: Use `--prompt "your customized prompt"` to specify a single prompt.
2. Multiple prompts: Create a JSON file and use `--prompt_file $json_path`. Create a JSON file containing your prompts and use --prompt_file $json_path to load them. The JSON file can follow this format:
```python
{
    0: "prompt1",
    1: "prompt2",
    ...
}
```

#### For [video-text alignment](#video-text-alignment) or [dynamic quality](#dynamic-quality) dimensions, `set mode=custom_nonstatic`:
```bash
python evaluate.py \
 --dimension $DIMENSION \ 
 --videos_path ./data/ \
 --mode custom_nonstatic \
 --config_path ./config.json \
 --models modelname1 modelname2
```
or
```bash
videobench \
 --dimension $DIMENSION \
 --videos_path ./data/ \
 --mode custom_nonstatic \
 --config_path ./config.json \
 --models modelname1 modelname2
```

#### For [static quality](#static-quality) dimensions, `set mode=custom_static`:
```bash
python evaluate.py \
 --dimension $DIMENSION \
 --videos_path ./data/ \
 --mode custom_static \
 --config_path ./config.json \
 --models modelname1 modelname2
```
or
```bash
videobench \
 --dimension $DIMENSION \
 --videos_path ./data/ \
 --mode custom_static \
 --config_path ./config.json \
 --models modelname1 modelname2
```

## Videos and Annotations

You can obtain the video data and human annotations in two ways:

### Option 1: Download from Hugging Face
- Videos dataset: [Video-Bench/Video-Bench_videos](https://huggingface.co/datasets/Video-Bench/Video-Bench_videos)
- Human annotations: [Video-Bench/Video-Bench_human_annotation](https://huggingface.co/datasets/Video-Bench/Video-Bench_human_annotation)

```bash
# Download videos
git clone https://huggingface.co/datasets/Video-Bench/Video-Bench_videos
# Download annotations  
git clone https://huggingface.co/datasets/Video-Bench/Video-Bench_human_annotation
```

### Option 2: Local Directory
The human annotations can also be found in the local directory:
```
./data/human_anno/
```

#### Additional Information  
- Manual annotation is conducted via a web interface, accessible at [https://github.com/Chenzhou2344/AnnoBoard.git].  

# Citation
If you use our dataset, code or find Video-Bench useful, please cite our paper in your work as:

```bib
@article{han2025video,
  title={Video-Bench: Human-Aligned Video Generation Benchmark},
  author={Han, Hui and Li, Siyuan and Chen, Jiaqi and Yuan, Yiwen and Wu, Yuling and Leong, Chak Tou and Du, Hanwen and Fu, Junchen and Li, Youhua and Zhang, Jie and others},
  journal={arXiv preprint arXiv:2504.04907},
  year={2025}
}
```

# Literature

## Video Generation Evaluation Methods

<table>
  <thead>
    <tr>
      <th>Model</th>
      <th>Paper</th>
      <th>Resource</th>
      <th>Conference/Journal/Preprint</th>
      <th>Year</th>
      <th style="width: 300px;">Features</th> <!-- 增加列宽 -->
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Video-Bench</td>
      <td><a href="xxx">Link</a></td>
      <td><a href="https://github.com/Video-Bench/Video-Bench/">GitHub</a></td>
      <td>Arxiv</td>
      <td>2024</td>
      <td>Video-Bench leverages Multimodal Large Language Models (MLLMs) to provide highly accurate evaluations that closely align with human preferences across multiple dimensions of video quality. It incorporates few-shot scoring and chain-of-query techniques, allowing for scalable and structured assessments. Video-Bench supports cross-modal consistency and offers more objective insights when diverging from human judgments, making it a more reliable and comprehensive tool for video generation evaluation. It also demonstrates unique strength compared to human ratings in terms of accuracy.</td>
    </tr>
    <tr>
      <td>FETV</td>
      <td><a href="https://proceedings.neurips.cc/paper_files/paper/2023/hash/c481049f7410f38e788f67c171c64ad5-Abstract-Datasets_and_Benchmarks.html">Link</a></td>
      <td><a href="https://github.com/llyx97/FETV">GitHub</a></td>
      <td>NeurIPS</td>
      <td>2023</td>
      <td>FETV is multi-aspect, categorizing the prompts based on three orthogonal aspects: the major content, the attributes to control and the prompt complexity.</td>
    </tr>
    <tr>
      <td>FVD</td>
      <td><a href="https://openreview.net/pdf?id=rylgEULtdN">Link</a></td>
      <td><a href="https://github.com/google-research/google-research/tree/master/frechet_video_distance">GitHub</a></td>
      <td>ICLR Workshop</td>
      <td>2023</td>
      <td>A novel metric for generative video models that extends the Fréchet Inception Distance (FID) to account for not only visual quality but also temporal coherence and diversity, addressing the lack of qualitative metrics in current video generation evaluation.</td>
    </tr>
    <tr>
      <td>GAIA</td>
      <td><a href="https://arxiv.org/abs/2406.06087">Link</a></td>
      <td><a href="https://github.com/zijianchen98/GAIA">GitHub</a></td>
      <td>Arxiv</td>
      <td>2024</td>
      <td>By adopting a causal reasoning perspective, it evaluates popular text-to-video (T2V) models on their ability to generate visually rational actions and benchmarks existing automatic evaluation methods, revealing a significant gap between current models and human perception patterns.</td>
    </tr>
    <tr>
      <td>SAVGBench</td>
      <td><a href="https://arxiv.org/abs/2412.13462">Link</a></td>
      <td><a href="https://drive.google.com/file/d/14Fy6C_N6BXymYKhXMxVbt7tHnZmVRMEd/view, https://www.aicrowd.com/challenges/sounding-video-generation-svg-challenge-2024/problems/spatial-alignment-track">Links</a></td>
      <td>Arxiv</td>
      <td>2024</td>
      <td>This work introduces a benchmark for Spatially Aligned Audio-Video Generation (SAVG), focusing on spatial alignment between audio and visuals. Key innovations include a new dataset, a baseline diffusion model for stereo audio-visual learning, and a spatial alignment metric, revealing significant gaps in quality and alignment between the model and ground truth.</td>
    </tr>
 <tr>
      <td>VBench++</td>
      <td><a href="https://arxiv.org/abs/2411.13503">Link</a></td>
      <td><a href="https://github.com/Vchitect/VBench">GitHub</a></td>
      <td>Arxiv</td>
      <td>2024</td>
      <td>VBench++ is a comprehensive benchmark for video generation, featuring 16 evaluation dimensions, human alignment validation, and support for both text-to-video and image-to-video models, assessing both technical quality and model trustworthiness.</td>
    </tr>
    <tr>
      <td>T2V-CompBench</td>
      <td><a href="https://arxiv.org/abs/2407.14505">Link</a></td>
      <td><a href="https://github.com/KaiyueSun98/T2V-CompBench">GitHub</a></td>
      <td>Arxiv</td>
      <td>2024</td>
      <td>T2V-CompBench evaluates diverse aspects such as attribute binding, spatial relationships, motion, and object interactions. It introduces tailored evaluation metrics based on MLLM, detection, and tracking, validated by human evaluation.</td>
    </tr>
    <tr>
      <td>VideoScore</td>
      <td><a href="https://aclanthology.org/2024.emnlp-main.127/">Link</a></td>
      <td><a href="https://tiger-ai-lab.github.io/VideoScore/">Website</a></td>
      <td>EMNLP</td>
      <td>2024</td>
      <td>It introduces a dataset with human-provided multi-aspect scores for 37.6K videos from 11 generative models. VideoScore is trained on this to provide automatic video quality assessment, achieving a 77.1 Spearman correlation with human ratings.</td>
    </tr>
    <tr>
      <td>ChronoMagic-Bench</td>
      <td><a href="https://arxiv.org/abs/2406.18522">Link</a></td>
      <td><a href="https://pku-yuangroup.github.io/ChronoMagic-Bench/">Website</a></td>
      <td>NeurIPS</td>
      <td>2024</td>
      <td>ChronoMagic-Bench evaluates T2V models on their ability to generate time-lapse videos with significant metamorphic amplitude and temporal coherence, using 1,649 prompts across four categories. Its advantages include the introduction of new metrics (MTScore and CHScore) and a large-scale dataset (ChronoMagic-Pro) for comprehensive, high-quality evaluation.</td>
    </tr>
    <tr>
      <td>T2VSafetyBench</td>
      <td><a href="https://arxiv.org/abs/2407.05965">Link</a></td>
      <td><a href="https://github.com/yibo-miao/T2VSafetyBench">GitHub</a></td>
      <td>NeurIPS</td>
      <td>2024</td>
      <td>T2VSafetyBench introduces a benchmark for assessing the safety of text-to-video models, focusing on 12 critical aspects of video generation safety, including temporal risks. It addresses the unique safety concerns of video generation, providing a malicious prompt dataset, and offering valuable insights into the trade-off between usability and safety.</td>
    </tr>
    <tr>
      <td>T2VBench</td>
      <td><a href="https://openaccess.thecvf.com/content/CVPR2024W/EvGenFM/html/Ji_T2VBench_Benchmarking_Temporal_Dynamics_for_Text-to-Video_Generation_CVPRW_2024_paper.html">Link</a></td>
      <td><a href="https://ji-pengliang.github.io/T2VBench/">Website</a></td>
      <td>CVPR</td>
      <td>2024</td>
      <td>T2VBench focuses on 16 critical temporal dimensions such as camera transitions and event sequences for evaluating text-to-video models, consisting of a hierarchical framework with over 1,600 prompts and 5,000 videos.</td>
    </tr>
    <tr>
      <td>EvalCrafter</td>
      <td><a href="https://openaccess.thecvf.com/content/CVPR2024/html/Liu_EvalCrafter_Benchmarking_and_Evaluating_Large_Video_Generation_Models_CVPR_2024_paper.html">Link</a></td>
      <td><a href="http://evalcrafter.github.io/">Website</a></td>
      <td>CVPR</td>
      <td>2024</td>
      <td>EvalCrafter provides a systematic framework for benchmarking and evaluating large-scale video generation models, ensuring high-quality assessments across various video generation attributes.</td>
    </tr>
<tr>
      <td>VQAScore</td>
      <td><a href="https://link.springer.com/chapter/10.1007/978-3-031-72673-6_20">Link</a></td>
      <td><a href="https://github.com/linzhiqiu/t2v_metrics">GitHub</a></td>
      <td>ECCV</td>
      <td>2024</td>
      <td>This work introduces VQAScore, a novel alignment metric that uses a visual-question-answering model to assess image-text coherence, addressing the limitations of CLIPScore with complex prompts. It also presents GenAI-Bench, a challenging benchmark of 1,600 compositional prompts and 15,000 human ratings, enabling more accurate evaluation of generative models like Stable Diffusion and DALL-E 3.</td>
    </tr>
    <tr>
      <td>VBench</td>
      <td><a href="https://openaccess.thecvf.com/content/CVPR2024/html/Huang_VBench_Comprehensive_Benchmark_Suite_for_Video_Generative_Models_CVPR_2024_paper.html">Link</a></td>
      <td><a href="https://github.com/Vchitect/VBench">GitHub</a></td>
      <td>CVPR</td>
      <td>2024</td>
      <td>VBench introduces a comprehensive evaluation benchmark for video generation, addressing the misalignment between current metrics and human perception. Its key innovations include 16 detailed evaluation dimensions, human preference alignment for validation, and the ability to assess various content types and model gaps.</td>
    </tr>
    <tr>
      <td>DEVIL</td>
      <td><a href="https://arxiv.org/abs/2407.01094">Link</a></td>
      <td><a href="https://github.com/MingXiangL/DEVIL">GitHub</a></td>
      <td>NeurIPS</td>
      <td>2024</td>
      <td>DEVIL introduces a new benchmark with dynamic scores at different temporal granularities, achieving over 90% Pearson correlation with human ratings for comprehensive model assessment.</td>
    </tr>
    <tr>
      <td>AIGCBench</td>
      <td><a href="https://arxiv.org/abs/2401.01651">Link</a></td>
      <td><a href="https://www.benchcouncil.org/AIGCBench">Website</a></td>
      <td>Arxiv</td>
      <td>2024</td>
      <td>AIGCBench is a benchmark for evaluating image-to-video (I2V) generation. It incorporates an open-domain image-text dataset and introduces 11 metrics across four dimensions—alignment, motion effects, temporal consistency, and video quality.</td>
    </tr>
    <tr>
      <td>MiraData</td>
      <td><a href="https://arxiv.org/abs/2407.06358">Link</a></td>
      <td><a href="https://github.com/mira-space/MiraData">GitHub</a></td>
      <td>NeurIPS</td>
      <td>2024</td>
      <td>MiraData offers longer videos, stronger motion intensity, and more detailed captions. Paired with MiraBench to enhance evaluation with metrics like 3D consistency and motion strength.</td>
    </tr>
    <tr>
      <td>PhyGenEval</td>
      <td><a href="https://arxiv.org/abs/2410.05363">Link</a></td>
      <td><a href="https://phygenbench123.github.io/">Website</a></td>
      <td>Arxiv</td>
      <td>2024</td>
      <td>PhyGenBench is designed to evaluate the understanding of physical commonsense in text-to-video (T2V) generation, consisting of 160 prompts covering 27 physical laws across four domains, paired with the PhyGenEval evaluation framework that enables assessments of models' adherence to physical commonsense.</td>
    </tr>
    <tr>
      <td>VideoPhy</td>
      <td><a href="https://arxiv.org/abs/2406.03520">Link</a></td>
      <td><a href="https://github.com/Hritikbansal/videophy">GitHub</a></td>
      <td>Arxiv</td>
      <td>2024</td>
      <td>VideoPhy is a benchmark designed to assess the physical commonsense accuracy of generated videos, particularly for T2V models, by evaluating their adherence to real-world physical laws and behaviors.</td>
    </tr>
    <tr>
      <td>T2VHE</td>
      <td><a href="https://arxiv.org/abs/2406.08845">Link</a></td>
      <td><a href="https://github.com/ztlmememe/T2VHE">GitHub</a></td>
      <td>Arxiv</td>
      <td>2024</td>
      <td>The T2VHE protocol is an approach for evaluating text-to-video (T2V) models, addressing challenges in reproducibility, reliability, and practicality of manual evaluations. It includes defined metrics, annotator training, and a dynamic evaluation module.</td>
    </tr>
  </tbody>
</table>

<!--
| Model             | Paper                                                                                                      | Resource                                                                                     | Conference/Journal/Preprint | Year | Features |
|-------------------|------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|-----------------------------|------|----------|
| Video-Bench              | [Link](xxx) | [GitHub](https://github.com/Video-Bench/Video-Bench/)                                                      | Arxiv                     | 2024 |      Video-Bench leverages Multimodal Large Language Models (MLLMs) to provide highly accurate evaluations that closely align with human preferences across multiple dimensions of video quality. It incorporates few-shot scoring and chain-of-query techniques, allowing for scalable and structured assessments. Video-Bench supports cross-modal consistency and offers more objective insights when diverging from human judgments, making it a more reliable and comprehensive tool for video generation evaluation. It also demonstrates unique strength compared to human ratings in terms of accuracy. |
| FETV              | [Link](https://proceedings.neurips.cc/paper_files/paper/2023/hash/c481049f7410f38e788f67c171c64ad5-Abstract-Datasets_and_Benchmarks.html) | [GitHub](https://github.com/llyx97/FETV)                                                      | NeurIPS                     | 2023 |      FETV is multi-aspect, categorizing the prompts based on three orthogonal aspects: the major content, the attributes to control and the prompt complexity.    |
| FVD               | [Link](https://openreview.net/pdf?id=rylgEULtdN)                                                             | [GitHub](https://github.com/google-research/google-research/tree/master/frechet_video_distance) | ICLR Workshop               | 2023 |     A novel metric for generative video models that extends the Fréchet Inception Distance (FID) to account for not only visual quality but also temporal coherence and diversity, addressing the lack of qualitative metrics in current video generation evaluation.     |
| GAIA              | [Link](https://arxiv.org/abs/2406.06087)                                                                     | [GitHub](https://github.com/zijianchen98/GAIA)                                               | Arxiv                       | 2024 |     By adopting a causal reasoning perspective, it evaluates popular text-to-video (T2V) models on their ability to generate visually rational actions and benchmarks existing automatic evaluation methods, revealing a significant gap between current models and human perception patterns.     |
| SAVGBench         | [Link](https://arxiv.org/abs/2412.13462)                                                                     | [Links](https://drive.google.com/file/d/14Fy6C_N6BXymYKhXMxVbt7tHnZmVRMEd/view, https://www.aicrowd.com/challenges/sounding-video-generation-svg-challenge-2024/problems/spatial-alignment-track) | Arxiv                       | 2024 |    This work introduces a benchmark for Spatially Aligned Audio-Video Generation (SAVG), focusing on spatial alignment between audio and visuals. Key innovations include a new dataset, a baseline diffusion model for stereo audio-visual learning, and a spatial alignment metric, revealing significant gaps in quality and alignment between the model and ground truth.      |
| VBench++          | [Link](https://arxiv.org/abs/2411.13503)                                                                     | [GitHub](https://github.com/Vchitect/VBench)                                                 | Arxiv                       | 2024 |     VBench++ is a comprehensive benchmark for video generation, featuring 16 evaluation dimensions, human alignment validation, and support for both text-to-video and image-to-video models, assessing both technical quality and model trustworthiness.     |
| T2V-CompBench     | [Link](https://arxiv.org/abs/2407.14505)                                                                     | [GitHub](https://github.com/KaiyueSun98/T2V-CompBench)                                       | Arxiv                       | 2024 |     T2V-CompBench evaluates diverse aspects such as attribute binding, spatial relationships, motion, and object interactions. It introduces tailored evaluation metrics based on MLLM, detection, and tracking, validated by human evaluation.      |
| VideoScore        | [Link](https://aclanthology.org/2024.emnlp-main.127/)                                                        | [Website](https://tiger-ai-lab.github.io/VideoScore/)                                         | EMNLP                       | 2024 |     It introduces a dataset with human-provided multi-aspect scores for 37.6K videos from 11 generative models. VideoScore is trained on this to provide automatic video quality assessment, achieving a 77.1 Spearman correlation with human ratings.     |
| ChronoMagic-Bench | [Link](https://arxiv.org/abs/2406.18522)                                                                     | [Website](https://pku-yuangroup.github.io/ChronoMagic-Bench/)                                 | NeurIPS                     | 2024 |      ChronoMagic-Bench evaluates T2V models on their ability to generate time-lapse videos with significant metamorphic amplitude and temporal coherence, using 1,649 prompts across four categories. Its advantages include the introduction of new metrics (MTScore and CHScore) and a large-scale dataset (ChronoMagic-Pro) for comprehensive, high-quality evaluation.    |
| T2VSafetyBench    | [Link](https://arxiv.org/abs/2407.05965)                                                                     | [GitHub](https://github.com/yibo-miao/T2VSafetyBench)                                        | NeurIPS                     | 2024 |     T2VSafetyBench introduces a benchmark for assessing the safety of text-to-video models, focusing on 12 critical aspects of video generation safety, including temporal risks. It addresses the unique safety concerns of video generation, providing a malicious prompt dataset, and offering valuable insights into the trade-off between usability and safety.     |
| T2VBench          | [Link](https://openaccess.thecvf.com/content/CVPR2024W/EvGenFM/html/Ji_T2VBench_Benchmarking_Temporal_Dynamics_for_Text-to-Video_Generation_CVPRW_2024_paper.html) | [Website](https://ji-pengliang.github.io/T2VBench/)                                           | CVPR                        | 2024 |     T2VBench focuses on 16 critical temporal dimensions such as camera transitions and event sequences for evaluating text-to-video models, consisting of a hierarchical framework with over 1,600 prompts and 5,000 videos.     |
| EvalCrafter       | [Link](https://openaccess.thecvf.com/content/CVPR2024/html/Liu_EvalCrafter_Benchmarking_and_Evaluating_Large_Video_Generation_Models_CVPR_2024_paper.html) | [Website](http://evalcrafter.github.io/)                                                     | CVPR                        | 2024 |     This work focuses on visual, content, motion quality, and text-video alignment, introducing a human alignment method that improves evaluation accuracy, offering higher correlation with user opinions than traditional metric averaging.     |
| VQAScore          | [Link](https://link.springer.com/chapter/10.1007/978-3-031-72673-6_20)                                        | [GitHub](https://github.com/linzhiqiu/t2v_metrics)                                           | ECCV                        | 2024 |     This work introduces VQAScore, a novel alignment metric that uses a visual-question-answering model to assess image-text coherence, addressing the limitations of CLIPScore with complex prompts. It also presents GenAI-Bench, a challenging benchmark of 1,600 compositional prompts and 15,000 human ratings, enabling more accurate evaluation of generative models like Stable Diffusion and DALL-E 3.     |
| VBench            | [Link](https://openaccess.thecvf.com/content/CVPR2024/html/Huang_VBench_Comprehensive_Benchmark_Suite_for_Video_Generative_Models_CVPR_2024_paper.html) | [GitHub](https://github.com/Vchitect/VBench)                                                 | CVPR                        | 2024 |     VBench introduces a comprehensive evaluation benchmark for video generation, addressing the misalignment between current metrics and human perception. Its key innovations include 16 detailed evaluation dimensions, human preference alignment for validation, and the ability to assess various content types and model gaps.     |
| DEVIL        | [Link](https://arxiv.org/abs/2407.01094)                                                                   | [GitHub](https://github.com/MingXiangL/DEVIL)                                                      | NeurIPS                     | 2024 |     DEVIL introduces a new benchmark with dynamic scores at different temporal granularities, achieving over 90% Pearson correlation with human ratings for comprehensive model assessment.     |
| AIGCBench    | [Link](https://arxiv.org/abs/2401.01651)                                                                   | [Website](https://www.benchcouncil.org/AIGCBench)                                                   | Arxiv                       | 2024 |     AIGCBench is a benchmark for evaluating image-to-video (I2V) generation. It incorporates a open-domain image-text dataset and introduces 11 metrics across four dimensions—alignment, motion effects, temporal consistency, and video quality.     |
| MiraData     | [Link](https://arxiv.org/abs/2407.06358)                                                                   | [GitHub](https://github.com/mira-space/MiraData)                                                   | NeurIPS                     | 2024 |     MiraData offers longer videos, stronger motion intensity, and more detailed captions. Paired with MiraBench to enhance evaluation with metrics like 3D consistency and motion strength.     |
| PhyGenEval   | [Link](https://arxiv.org/abs/2410.05363)                                                                   | [Website](https://phygenbench123.github.io/)                                                       | Arxiv                       | 2024 |     PhyGenBench is designed to evaluate the understanding of physical commonsense in text-to-video (T2V) generation, consisting of 160 prompts covering 27 physical laws across four domains, paired with the PhyGenEval evaluation framework that enables assessments of models' adherence to physical commonsense.     |
| VideoPhy     | [Link](https://arxiv.org/abs/2406.03520)                                                                   | [GitHub](https://github.com/Hritikbansal/videophy)                                                 | Arxiv                       | 2024 |     VideoPhy is a benchmark designed to assess the physical commonsense accuracy of text-to-video generative models by evaluating how well generated videos follow real-world physical interactions across various material types, highlighting significant gaps of current models in simulating the physical world.     |
| T2VHE        | [Link](https://arxiv.org/abs/2406.08845)                                                                   | [GitHub](https://github.com/ztlmememe/T2VHE)                                                      | Arxiv                       | 2024 |     The T2VHE protocol is a approach for evaluating text-to-video (T2V) models, addressing challenges in reproducibility, reliability, and practicality of manual evaluations. It includes defined metrics, annotator training, and a dynamic evaluation module.     |
-->

