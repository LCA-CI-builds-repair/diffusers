import warnings

from diffusers import StableDiffusionInpaintPipeline as StableDiffusionInpaintPipeline  # noqa F401

import warnings

warnings.warn(
    "The `inpainting.py` script is outdated. Please use `from diffusers import StableDiffusionInpaintPipeline` instead."
)