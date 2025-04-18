import torch
from typing import Union

def get_device() -> str:
    """Get the appropriate device for model inference."""
    if torch.backends.mps.is_available():
        return "mps"
    elif torch.cuda.is_available():
        return "cuda"
    return "cpu"

def format_response(response: str) -> str:
    """Format the model's response for better readability."""
    return response.strip()

def validate_input(prompt: str) -> Union[str, None]:
    """Validate the input prompt."""
    if not prompt or len(prompt.strip()) == 0:
        return None
    return prompt.strip() 