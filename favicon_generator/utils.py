"""Utility functions for favicon generator."""
from pathlib import Path
from typing import Tuple, Optional
from PIL import Image
from rich.console import Console

console = Console()

def validate_image_dimensions(img: Image.Image) -> Tuple[bool, str]:
    """Validate if the image meets the recommended requirements.
    
    Args:
        img: PIL Image object to validate
        
    Returns:
        Tuple of (is_valid, message)
    """
    width, height = img.size
    messages = []
    
    if width != height:
        messages.append("⚠️  A imagem não é quadrada. Ela pode ficar distorcida.")
    
    if width < 512 or height < 512:
        messages.append("⚠️  A resolução é menor que 512x512. A qualidade pode ficar ruim.")
    
    is_valid = len(messages) == 0
    return is_valid, "\n".join(messages)

def ensure_output_dir(output_dir: str) -> Path:
    """Ensure the output directory exists.
    
    Args:
        output_dir: Path to the output directory
        
    Returns:
        Path object of the output directory
    """
    path = Path(output_dir)
    path.mkdir(parents=True, exist_ok=True)
    return path

def get_image_format(path: str) -> Optional[str]:
    """Get the image format from file extension.
    
    Args:
        path: Path to the image file
        
    Returns:
        Format string (e.g., 'PNG', 'JPEG', 'SVG') or None if unsupported
    """
    ext = Path(path).suffix.lower()
    if ext in ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp']:
        return ext[1:].upper()
    elif ext == '.svg':
        return 'SVG'
    return None
