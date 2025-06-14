"""Generate HTML metadata and web app manifest."""
from pathlib import Path
from typing import Optional
import json

def generate_html_metadata(output_dir: str, manifest_generated: bool = False) -> str:
    """Generate HTML metadata for favicons.
    
    Args:
        output_dir: Directory where favicons are stored
        manifest_generated: Whether a web app manifest was generated
        
    Returns:
        HTML string with meta tags
    """
    metadata_parts = [
        "<!-- Favicon metadata -->",
        f'<link rel="apple-touch-icon" sizes="180x180" href="/{output_dir}/apple-touch-icon.png">',
        f'<link rel="icon" type="image/png" sizes="32x32" href="/{output_dir}/favicon-32x32.png">',
        f'<link rel="icon" type="image/png" sizes="16x16" href="/{output_dir}/favicon-16x16.png">',
        f'<link rel="icon" href="/{output_dir}/favicon.ico" type="image/x-icon">'
    ]
    
    if manifest_generated:
        metadata_parts.append(f'<link rel="manifest" href="/{output_dir}/site.webmanifest">')
        
    metadata_parts.extend([
        '<meta name="msapplication-TileColor" content="#ffffff">',
        '<meta name="theme-color" content="#ffffff">'
    ])
    
    return "\n".join(metadata_parts).strip()

def generate_manifest(
    output_dir: str,
    name: str = "App",
    short_name: Optional[str] = None,
    theme_color: str = "#ffffff",
    background_color: str = "#ffffff",
    start_url: str = "/"
) -> dict:
    """Generate a web app manifest.
    
    Args:
        output_dir: Directory where favicons are stored
        name: Full name of the application
        short_name: Short name for the application (defaults to name)
        theme_color: Theme color in hex format
        background_color: Background color in hex format
        start_url: Start URL for the application
        
    Returns:
        Dictionary with manifest data
    """
    if short_name is None:
        short_name = name
        
    return {
        "name": name,
        "short_name": short_name,
        "icons": [
            {
                "src": f"/{output_dir}/android-chrome-192x192.png",
                "sizes": "192x192",
                "type": "image/png"
            },
            {
                "src": f"/{output_dir}/android-chrome-512x512.png",
                "sizes": "512x512",
                "type": "image/png"
            }
        ],
        "start_url": start_url,
        "display": "standalone",
        "background_color": background_color,
        "theme_color": theme_color
    }

def save_manifest(manifest_data: dict, output_dir: str) -> Path:
    """Save manifest data to a file.
    
    Args:
        manifest_data: Dictionary with manifest data
        output_dir: Directory to save the manifest file
        
    Returns:
        Path to the saved manifest file
    """
    output_path = Path(output_dir) / "site.webmanifest"
    with open(output_path, 'w') as f:
        json.dump(manifest_data, f, indent=2)
    return output_path
