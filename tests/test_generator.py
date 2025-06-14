"""Tests for favicon generator."""
import os
import shutil
from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest
from PIL import Image

from favicon_generator.generator import generate_favicon, load_image, FAVICON_SIZES
from favicon_generator.utils import validate_image_dimensions


def create_test_image(path: str, size: tuple[int, int] = (512, 512)) -> None:
    """Create a test image file."""
    img = Image.new('RGB', size, color='red')
    img.save(path)


class TestGenerator:
    """Test favicon generator functionality."""

    @pytest.fixture(autouse=True)
    def setup(self, tmp_path):
        """Set up test environment."""
        self.test_dir = tmp_path / "test_output"
        self.test_dir.mkdir()
        self.test_image = self.test_dir / "test.png"
        create_test_image(str(self.test_image))
        yield
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_load_image_png(self):
        """Test loading a PNG image."""
        img = load_image(str(self.test_image))
        assert img.size == (512, 512)
        assert img.mode == 'RGBA'

    @patch('favicon_generator.generator.cairosvg.svg2png')
    def test_load_image_svg(self, mock_svg2png, tmp_path):
        """Test loading an SVG image."""
        # Create a mock SVG
        svg_path = tmp_path / "test.svg"
        svg_path.write_text("<svg></svg>")
        
        # Mock the SVG to PNG conversion
        mock_svg2png.return_value = b'PNG_DATA'
        
        img = load_image(str(svg_path))
        assert img is not None
        mock_svg2png.assert_called_once()

    def test_generate_favicon_default(self):
        """Test generating favicons with default settings."""
        img = Image.open(self.test_image).convert('RGBA')
        output_dir = str(self.test_dir / "output")
        
        generated_files = generate_favicon(img, output_dir)
        
        # Check if all expected files were generated
        expected_files = [
            'favicon.ico',
            'favicon-16x16.png',
            'favicon-32x32.png',
            'favicon-48x48.png',
            'favicon-96x96.png',
            'apple-touch-icon.png',
            'android-chrome-192x192.png',
            'android-chrome-512x512.png',
        ]
        
        assert len(generated_files) == len(expected_files)
        for filename in expected_files:
            assert (Path(output_dir) / filename).exists(), f"{filename} was not generated"

    def test_generate_favicon_webp(self):
        """Test generating WebP versions."""
        img = Image.open(self.test_image).convert('RGBA')
        output_dir = str(self.test_dir / "output_webp")
        
        generate_favicon(img, output_dir, webp=True)
        
        # Check if WebP versions were generated
        for size, _ in FAVICON_SIZES:
            webp_path = Path(output_dir) / f"favicon-{size}x{size}.webp"
            assert webp_path.exists(), f"WebP version not generated for {size}x{size}"

    def test_generate_favicon_avif(self):
        """Test generating AVIF versions (if supported)."""
        img = Image.open(self.test_image).convert('RGBA')
        output_dir = str(self.test_dir / "output_avif")
        
        try:
            generate_favicon(img, output_dir, avif=True)
            
            # Check if AVIF versions were generated (if supported)
            for size, _ in FAVICON_SIZES:
                avif_path = Path(output_dir) / f"favicon-{size}x{size}.avif"
                # AVIF might not be supported in test environment
                if hasattr(Image, 'AVIF'):
                    assert avif_path.exists(), f"AVIF version not generated for {size}x{size}"
        except Exception as e:
            if "encoder error" not in str(e).lower():
                raise
            # AVIF not supported in test environment, which is okay


class TestValidation:
    """Test image validation functions."""
    
    def test_validate_image_dimensions_square(self):
        """Test validation of square images."""
        img = Image.new('RGB', (512, 512))
        is_valid, message = validate_image_dimensions(img)
        assert is_valid is True
        assert message == ""
    
    def test_validate_image_dimensions_not_square(self):
        """Test validation of non-square images."""
        img = Image.new('RGB', (512, 256))
        is_valid, message = validate_image_dimensions(img)
        assert is_valid is False
        assert "não é quadrada" in message
    
    def test_validate_image_dimensions_small(self):
        """Test validation of small images."""
        img = Image.new('RGB', (256, 256))
        is_valid, message = validate_image_dimensions(img)
        assert is_valid is False
        assert "menor que 512x512" in message
