# Referência da API

Este documento descreve a API pública do módulo `favicon_generator` para uso programático.

## Visão Geral

O Favicon Generator pode ser usado como uma biblioteca Python para gerar favicons e ativos da web programaticamente.

## Módulo `favicon_generator`

### Funções Principais

#### `generate_favicons`

Gera favicons e ativos da web a partir de uma imagem de entrada.

```python
def generate_favicons(
    image_path: Union[str, Path],
    output_dir: Union[str, Path] = "favicons",
    manifest: bool = True,
    optimize: bool = False,
    webp: bool = False,
    avif: bool = False,
    app_name: str = "My App",
    app_short_name: Optional[str] = None,
    theme_color: str = "#ffffff",
    background_color: str = "#ffffff",
) -> Dict[str, str]:
    """
    Gera favicons e ativos da web a partir de uma imagem.

    Args:
        image_path: Caminho para a imagem de origem
        output_dir: Diretório de saída para os arquivos gerados
        manifest: Se True, gera o arquivo site.webmanifest
        optimize: Se True, otimiza as imagens com Squoosh CLI
        webp: Se True, gera versões WebP dos ícones
        avif: Se True, gera versões AVIF dos ícones
        app_name: Nome do aplicativo para o manifesto
        app_short_name: Nome curto do aplicativo (opcional)
        theme_color: Cor do tema para o manifesto
        background_color: Cor de fundo para o manifesto

    Returns:
        Dicionário com caminhos dos arquivos gerados
    """
```

#### `generate_html_metadata`

Gera o código HTML com as tags de metadados para favicons e manifestos.

```python
def generate_html_metadata(
    output_dir: Union[str, Path] = "favicons",
    include_manifest: bool = True,
) -> str:
    """
    Gera o código HTML com as tags de metadados.

    Args:
        output_dir: Diretório base para os caminhos dos arquivos
        include_manifest: Se True, inclui o link para o manifesto

    Returns:
        String com o código HTML
    """
```

### Classes Principais

#### `FaviconGenerator`

Classe principal para geração de favicons.

```python
class FaviconGenerator:
    """Gerencia a geração de favicons e ativos da web."""
    
    def __init__(
        self,
        image_path: Union[str, Path],
        output_dir: Union[str, Path] = "favicons",
        manifest: bool = True,
        optimize: bool = False,
        webp: bool = False,
        avif: bool = False,
        app_name: str = "My App",
        app_short_name: Optional[str] = None,
        theme_color: str = "#ffffff",
        background_color: str = "#ffffff",
    ):
        """
        Inicializa o gerador de favicons.

        Args:
            image_path: Caminho para a imagem de origem
            output_dir: Diretório de saída
            manifest: Se True, gera o manifesto do aplicativo
            optimize: Se True, otimiza as imagens
            webp: Se True, gera versões WebP
            avif: Se True, gera versões AVIF
            app_name: Nome do aplicativo
            app_short_name: Nome curto do aplicativo
            theme_color: Cor do tema
            background_color: Cor de fundo
        """
    
    def generate(self) -> Dict[str, str]:
        """
        Gera todos os arquivos de favicon e ativos.

        Returns:
            Dicionário com caminhos dos arquivos gerados
        """
    
    def generate_manifest(self) -> str:
        """
        Gera o arquivo de manifesto do aplicativo.

        Returns:
            Caminho para o arquivo de manifesto gerado
        """
    
    def generate_html_metadata(self) -> str:
        """
        Gera o código HTML com as tags de metadados.

        Returns:
            String com o código HTML
        """
```

## Exemplos de Uso

### Exemplo 1: Uso Básico

```python
from favicon_generator import generate_favicons, generate_html_metadata

# Gerar favicons
files = generate_favicons(
    "logo.png",
    output_dir="static/favicons",
    app_name="Meu Aplicativo",
    theme_color="#4f46e5"
)

# Obter HTML de metadados
html_metadata = generate_html_metadata("static/favicons")
print(html_metadata)
```

### Exemplo 2: Uso com a Classe FaviconGenerator

```python
from favicon_generator import FaviconGenerator
from pathlib import Path

# Criar instância do gerador
generator = FaviconGenerator(
    image_path=Path("assets/logo.png"),
    output_dir=Path("public/favicons"),
    webp=True,
    avif=True,
    app_name="Meu Aplicativo",
    theme_color="#4f46e5"
)

# Gerar todos os arquivos
generated_files = generator.generate()

# Obter HTML de metadados
html_metadata = generator.generate_html_metadata()

# Salvar o HTML em um arquivo
with open("templates/includes/favicons.html", "w") as f:
    f.write(html_metadata)
```

## Tratamento de Erros

O módulo define as seguintes exceções personalizadas:

- `FaviconGeneratorError`: Classe base para todos os erros do gerador
- `InvalidImageError`: Erro lançado quando a imagem de entrada é inválida
- `ImageProcessingError`: Erro durante o processamento da imagem
- `OptimizationError`: Erro durante a otimização de imagens

## Tipos de Dados

### `IconSize`

```python
class IconSize(NamedTuple):
    """Representa um tamanho de ícone."""
    width: int
    height: int
    
    @property
    def filename(self) -> str:
        """Retorna o nome do arquivo para este tamanho."""
        return f"favicon-{self.width}x{self.height}.png"
```

### `GeneratedFiles`

```python
GeneratedFiles = Dict[str, str]  # Nome do arquivo → caminho completo
```

## Constantes

### `DEFAULT_SIZES`

```python
DEFAULT_SIZES: List[IconSize] = [
    IconSize(16, 16),
    IconSize(32, 32),
    IconSize(48, 48),
    IconSize(96, 96),
    IconSize(192, 192),  # Android Chrome
    IconSize(512, 512),  # Android Chrome (HD)
]
```

### `APPLE_TOUCH_ICON_SIZE`

```python
APPLE_TOUCH_ICON_SIZE: IconSize = IconSize(180, 180)  # Tamanho para Apple Touch Icon
```
