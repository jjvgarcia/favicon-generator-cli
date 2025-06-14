"""Core functionality for favicon generation."""
from pathlib import Path
from typing import List, Tuple, Optional
from PIL import Image
import cairosvg
import io

# Standard favicon sizes and their respective filenames
FAVICON_SIZES = [
    (16, "favicon-16x16.png"),
    (32, "favicon-32x32.png"),
    (48, "favicon-48x48.png"),
    (96, "favicon-96x96.png"),
    (180, "apple-touch-icon.png"),
    (192, "android-chrome-192x192.png"),
    (512, "android-chrome-512x512.png"),
]

def load_image(image_path: str) -> Image.Image:
    """Load an image from file, supporting both SVG and raster formats.
    
    Args:
        image_path: Path to the input image
        
    Returns:
        PIL Image object
    """
    path = Path(image_path)
    if path.suffix.lower() == '.svg':
        # Convert SVG to PNG in memory
        png_data = cairosvg.svg2png(url=str(path))
        return Image.open(io.BytesIO(png_data)).convert("RGBA")
    return Image.open(path).convert("RGBA")

def generate_favicon(
    img: Image.Image,
    output_dir: str,
    webp: bool = False,
    avif: bool = False
) -> List[Path]:
    """Generate favicon files in various sizes and formats.
    
    Args:
        img: Input image as PIL Image
        output_dir: Directory to save generated files
        webp: Whether to generate WebP versions
        avif: Whether to generate AVIF versions
        
    Returns:
        List of generated file paths
    """
    generated_files = []
    output_path = Path(output_dir)
    
    # Prepare list of images for ICO
    ico_images = []
    
    for size, filename in FAVICON_SIZES:
        # Resize image
        resized = img.resize((size, size), Image.LANCZOS)
        
        # Save PNG
        png_path = output_path / filename
        resized.save(png_path, format="PNG")
        generated_files.append(png_path)
        
        # Save variants if requested
        if webp or avif:
            base_name = png_path.stem
            if webp:
                webp_path = output_path / f"{base_name}.webp"
                resized.save(webp_path, format="WEBP")
                generated_files.append(webp_path)
            
            if avif:
                try:
                    avif_path = output_path / f"{base_name}.avif"
                    resized.save(avif_path, format="AVIF")
                    generated_files.append(avif_path)
                except Exception as e:
                    print(f"⚠️  Could not generate AVIF for {base_name}: {e}")
        
        # Add to ICO sources if size is suitable
        if size in [16, 32, 48]:
            ico_images.append(resized)
    
    # Generate ICO file if we have images for it
    if ico_images:
        ico_path = output_path / "favicon.ico"
        ico_images[0].save(
            ico_path,
            format="ICO",
            sizes=[(img.width, img.height) for img in ico_images]
        )
        generated_files.append(ico_path)
    
    return generated_files
