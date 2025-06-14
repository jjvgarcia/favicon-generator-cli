# API Reference

## `favicon_generator.generate`

Generate favicons and web app icons from a source image.

```python
def generate(
    image_path: str,
    output_dir: str = "favicons",
    manifest: bool = True,
    optimize: bool = False,
    webp: bool = False,
    avif: bool = False,
    app_name: str = "My App",
    app_short_name: Optional[str] = None,
    theme_color: str = "#ffffff",
    background_color: str = "#ffffff",) -> None:
    """Generate favicons and web app icons.
    
    Args:
        image_path: Path to the source image file
        output_dir: Output directory for generated files
        manifest: Whether to generate web app manifest
        optimize: Optimize PNG files using Squoosh CLI
        webp: Generate WebP versions of all icons
        avif: Generate AVIF versions of all icons (requires Pillow with AVIF support)
        app_name: Application name for web app manifest
        app_short_name: Short application name (defaults to app_name)
        theme_color: Theme color for web app manifest
        background_color: Background color for web app manifest
    """
    ...
