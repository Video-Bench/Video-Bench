from .prompt.overall_consistency import *
from .prompt.color import *
from .prompt.object_class import *
from .prompt.scene import *
from .prompt.action import *
from .prompt.PromptTemplate4GPTeval import Prompt4ImagingQuality
from .prompt.PromptTemplate4GPTeval import Prompt4AestheticQuality
from .prompt.PromptTemplate4GPTeval import Prompt4TemporalConsistency
from .prompt.PromptTemplate4GPTeval import Prompt4MotionEffects


prompt = {
    "overall_consistency": overall_consistency_prompt,
    "color": color_prompt,
    "object_class": object_class_prompt,
    "scene": scene_prompt,
    "action": action_prompt,
    "imaging_quality": Prompt4ImagingQuality,
    "aesthetic_quality": Prompt4AestheticQuality,
    "temporal_consistency": Prompt4TemporalConsistency,
    "motion_effects": Prompt4MotionEffects
 }