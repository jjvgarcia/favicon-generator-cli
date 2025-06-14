"""Command-line interface for favicon generator."""
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.table import Table

from . import (
    __version__,
    load_image,
    generate_favicon,
    generate_html_metadata,
    generate_manifest,
    save_manifest,
    optimize_with_squoosh,
    validate_image_dimensions,
    ensure_output_dir,
    FAVICON_SIZES
)

app = typer.Typer(name="favicon-generator", add_completion=False)
console = Console()


def show_welcome():
    """Display welcome message and version."""
    console.rule("[bold blue]Favicon Generator")
    console.print(f"[dim]Version: {__version__}[/dim]\n")


def show_output_table(files, output_dir: Path):
    """Display a table of generated files with their sizes."""
    if not files:
        return

    table = Table(title="Generated Files", show_header=True, header_style="bold magenta")
    table.add_column("File", style="dim", width=40)
    table.add_column("Size", justify="right")
    
    for file in sorted(files):
        try:
            size = file.stat().st_size
            size_kb = size / 1024
            if size_kb < 1024:
                size_str = f"{size_kb:.1f} KB"
            else:
                size_str = f"{size_kb/1024:.1f} MB"
            
            # Show relative path to output directory
            rel_path = file.relative_to(output_dir)
            table.add_row(str(rel_path), size_str)
        except Exception as e:
            console.print(f"[yellow]Warning: Could not get info for {file}: {e}[/yellow]")
    
    console.print()
    console.print(table)


@app.command()
def generate(
    image_path: str = typer.Argument(..., help="Path to the source image (PNG, JPG, SVG, etc.)"),
    output_dir: str = typer.Option(
        "favicons",
        "--output", "-o",
        help="Output directory for generated files"
    ),
    manifest: bool = typer.Option(
        True,
        help="Generate a web app manifest (site.webmanifest)"
    ),
    optimize: bool = typer.Option(
        False,
        help="Optimize PNG files using Squoosh CLI (requires Node.js and @squoosh/cli)"
    ),
    webp: bool = typer.Option(
        False,
        help="Generate WebP versions of all icons"
    ),
    avif: bool = typer.Option(
        False,
        help="Generate AVIF versions of all icons (requires Pillow with AVIF support)"
    ),
    app_name: str = typer.Option(
        "My App",
        "--app-name",
        help="Application name for the web manifest"
    ),
    app_short_name: Optional[str] = typer.Option(
        None,
        "--app-short-name",
        help="Short application name (defaults to app_name)"
    ),
    theme_color: str = typer.Option(
        "#ffffff",
        help="Theme color for the web manifest"
    ),
    background_color: str = typer.Option(
        "#ffffff",
        help="Background color for the web manifest"
    ),
):
    """Generate favicons and web app assets from an image."""
    show_welcome()
    
    # Ensure output directory exists
    output_path = ensure_output_dir(output_dir)
    
    # Load and validate the source image
    try:
        console.print(f"[bold]Source image:[/bold] {image_path}")
        img = load_image(image_path)
        
        # Validate image dimensions
        is_valid, message = validate_image_dimensions(img)
        if not is_valid:
            console.print(f"[yellow]{message}[/yellow]")
        
        console.print(f"[green]✓ Loaded image: {img.width}x{img.height} pixels[/green]")
    except Exception as e:
        console.print(f"[red]Error loading image: {e}[/red]")
        raise typer.Exit(1)
    
    # Generate favicons
    try:
        console.print("\n[bold]Generating favicons...[/bold]")
        generated_files = generate_favicon(img, output_dir, webp=webp, avif=avif)
        console.print(f"[green]✓ Generated {len(generated_files)} files[/green]")
    except Exception as e:
        console.print(f"[red]Error generating favicons: {e}[/red]")
        raise typer.Exit(1)
    
    # Generate HTML metadata
    manifest_was_generated = False # Flag to track if manifest was actually created
    if manifest:
        try:
            manifest_data = generate_manifest(
                output_dir=output_dir,
                name=app_name,
                short_name=app_short_name,
                theme_color=theme_color,
                background_color=background_color
            )
            manifest_path = save_manifest(manifest_data, output_dir)
            generated_files.append(manifest_path)
            console.print("[green]✓ Generated web app manifest[/green]")
            manifest_was_generated = True
        except Exception as e:
            console.print(f"[yellow]Warning: Could not generate web manifest: {e}[/yellow]")

    try:
        metadata = generate_html_metadata(output_dir, manifest_generated=manifest_was_generated)
        metadata_path = output_path / "metadata.html"
        metadata_path.write_text(metadata)
        generated_files.append(metadata_path)
        console.print("[green]✓ Generated HTML metadata[/green]")
    except Exception as e:
        console.print(f"[yellow]Warning: Could not generate HTML metadata: {e}[/yellow]")
    

    
    # Optimize images if requested
    if optimize:
        console.print("\n[bold]Optimizing images...[/bold]")
        success = optimize_with_squoosh(output_dir)
        if success:
            console.print("[green]✓ Optimization complete[/green]")
        else:
            console.print("[yellow]Some optimizations may have failed[/yellow]")
    
    # Show summary
    console.print("\n[bold]🎉 Generation complete![/bold]")
    show_output_table(generated_files, output_path)
    
    console.print("\n[dim]Tip: Add the contents of metadata.html to your website's <head> section.[/dim]")


@app.command()
def version():
    """Show version information."""
    console.print(f"[bold]Favicon Generator[/bold] v{__version__}")


if __name__ == "__main__":
    app()
