"""Favicon Generator - Generate favicons and web app assets from a single image."""

from .generator import load_image, generate_favicon, FAVICON_SIZES
from .metadata import generate_html_metadata, generate_manifest, save_manifest
from .optimizer import optimize_with_squoosh
from .utils import validate_image_dimensions, ensure_output_dir, get_image_format

__version__ = "0.2.0"
__all__ = [
    'load_image',
    'generate_favicon',
    'generate_html_metadata',
    'generate_manifest',
    'save_manifest',
    'optimize_with_squoosh',
    'validate_image_dimensions',
    'ensure_output_dir',
    'get_image_format',
    'FAVICON_SIZES',
]