# Favicon Generator CLI

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/github/license/jjvgarcia/favicon-generator-cli)
![Stars](https://img.shields.io/github/stars/jjvgarcia/favicon-generator-cli?style=social)
![Issues](https://img.shields.io/github/issues/jjvgarcia/favicon-generator-cli)
![Last Commit](https://img.shields.io/github/last-commit/jjvgarcia/favicon-generator-cli)

A simple and powerful CLI tool to generate favicons, webmanifest, and metadata for web projects directly from an image (SVG, PNG, JPG).

## 🚀 Features

- ✅ Generate favicons in multiple sizes (16x16, 32x32, 48x48, 96x96, 180x180, 192x192, 512x512)
- ✅ Create `favicon.ico` (multi-resolution)
- ✅ Generate `site.webmanifest`
- ✅ Generate metadata HTML block ready for web projects
- ✅ Optional optimization with Squoosh (PNG compression)
- ✅ Supports WebP and AVIF variants
- ✅ Supports input in SVG, PNG, JPG
- ✅ Works fully offline — no need for online tools

## 📦 Installation

### Using virtual environment (recommended)

```bash
git clone https://github.com/jjvgarcia/favicon-generator-cli.git
cd favicon-generator-cli
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
```

## 🎯 Usage

```bash
favicon-generator generate logo.svg
```

### Example:

```bash
favicon-generator generate logo.svg --output-dir favicons --manifest --optimize --webp --avif
```

### Output files:

* `favicon.ico` (multi-resolution)
* PNGs:
  * favicon-16x16.png
  * favicon-32x32.png
  * favicon-48x48.png
  * favicon-96x96.png
  * apple-touch-icon.png (180x180)
  * android-chrome-192x192.png
  * android-chrome-512x512.png
* `site.webmanifest`
* `metadata.html`

## 🛠️ Options

```bash
favicon-generator generate --help
```

## 💡 Why a CLI tool?

* ✅ Works fully offline
* ✅ No need to depend on third-party websites
* ✅ Privacy — your logo never leaves your machine
* ✅ Easily automatable in CI/CD pipelines

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.
