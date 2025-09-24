"""
ComfyUI Prompt Iterator Extension
A custom node for iterating through multiple prompts with automatic filename generation
Author: BiloxiStudios Inc - BizaNator
Version: 2.1.0
"""

from .prompt_iterator import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

__version__ = "2.1.0"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]

# Extension metadata
WEB_DIRECTORY = "./js"

print("=" * 50)
print("ComfyUI Prompt Iterator v2.1.0")
print("BiloxiStudios Inc - BizaNator")
print("Loaded 3 custom nodes for prompt iteration")
print("=" * 50)