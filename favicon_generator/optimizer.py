"""Image optimization functionality using external tools."""
import subprocess
from pathlib import Path
from typing import List, Optional
from rich.console import Console

console = Console()

def optimize_with_squoosh(
    input_path: str,
    output_dir: Optional[str] = None,
    quality: int = 90,
    level: int = 4
) -> bool:
    """Optimize images using Squoosh CLI.
    
    Args:
        input_path: Path to the input file or directory
        output_dir: Directory to save optimized files (defaults to input directory)
        quality: Quality setting (1-100)
        level: Compression level (1-6, higher = better but slower)
        
    Returns:
        bool: True if optimization was successful, False otherwise
    """
    try:
        input_path = Path(input_path)
        if not input_path.exists():
            console.print(f"[red]Error: Input path does not exist: {input_path}[/red]")
            return False
            
        # If input is a directory, process all PNG files in it
        if input_path.is_dir():
            files = list(input_path.glob("*.png"))
            if not files:
                console.print(f"[yellow]No PNG files found in {input_path}[/yellow]")
                return False
        else:
            if input_path.suffix.lower() != '.png':
                console.print("[yellow]Squoosh optimization currently only supports PNG files[/yellow]")
                return False
            files = [input_path]
        
        output_dir = Path(output_dir) if output_dir else input_path if input_path.is_dir() else input_path.parent
        output_dir.mkdir(parents=True, exist_ok=True)
        
        console.print("[yellow]Optimizing images with Squoosh...[/yellow]")
        
        for file in files:
            output_file = output_dir / file.name
            try:
                # Squoosh CLI will create a .squooshed directory by default
                subprocess.run(
                    [
                        "squoosh-cli",
                        "--oxipng", str(level),
                        "--output-dir", str(output_dir),
                        str(file)
                    ],
                    check=True,
                    capture_output=True,
                    text=True
                )
                console.print(f"[green]Optimized:[/green] {file.name}")
            except subprocess.CalledProcessError as e:
                console.print(f"[red]Error optimizing {file.name}: {e.stderr}[/red]")
                return False
            except FileNotFoundError:
                console.print("[red]Squoosh CLI not found. Install with: npm install -g @squoosh/cli[/red]")
                return False
        
        return True
        
    except Exception as e:
        console.print(f"[red]Error during optimization: {str(e)}[/red]")
        return False
