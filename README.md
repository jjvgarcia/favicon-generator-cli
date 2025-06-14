# Favicon Generator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Uma ferramenta de linha de comando para gerar favicons e recursos de aplicativos da web a partir de uma única imagem. Suporta múltiplos formatos (PNG, SVG, JPG, etc.) e gera todos os arquivos necessários para aplicações web modernas.

## ✨ Recursos

- 🎨 Gere favicons em múltiplos tamanhos (16x16 a 512x512)
- 🌟 Crie variantes WebP e AVIF para melhor desempenho
- 📱 Gere ícones de aplicativos da web para iOS/Android
- 📝 Geração automática de metadados HTML
- 🏷️ Geração de Manifesto de Aplicativo da Web (`site.webmanifest`)
- ⚡ Otimização opcional de imagens com Squoosh CLI
- 🎯 Validação de entrada e avisos
- 📊 Saída de console elegante com Rich
- 🐍 Dicas de tipo e Python moderno

## 🚀 Instalação

### Usando pip (recomendado, quando publicado)

Após a publicação no PyPI, você poderá instalar com:
```bash
pip install favicon-generator
```

### A partir do código-fonte

1.  Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/favicon-generator.git
    cd favicon-generator
    ```

2.  Crie um ambiente virtual (opcional, mas recomendado):
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # Linux/macOS
    # ou: .venv\Scripts\activate    # Windows
    ```

3.  Instale o pacote (isso também instalará as dependências definidas em `pyproject.toml`):
    ```bash
    pip install .
    ```
    Para desenvolvimento, use o modo editável:
    ```bash
    pip install -e '.[dev]'
    ```
    A opção `[dev]` instala dependências adicionais para desenvolvimento e testes.

### Dependências Opcionais

-   **Otimização de Imagem com Squoosh CLI** (requer Node.js):
    ```bash
    npm install -g @squoosh/cli
    ```

## ⚙️ Uso

### Uso Básico

```bash
favicon-generator generate caminho/para/seu/logo.png
```

### Uso Avançado

```bash
favicon-generator generate caminho/para/logo.svg \
  --output-dir estaticos/favicons \
  --webp \
  --avif \
  --optimize \
  --app-name "Meu Aplicativo Incrível" \
  --theme-color "#2563eb" \
  --background-color "#ffffff"
```

### Opções do Comando

```
╭─ Argumentos ───────────────────────────────────────────────────────────╮
│ *    image_path      CAMINHO  Caminho para a imagem de origem         │
│                                (PNG, JPG, SVG, etc.) [obrigatório]    │
╰───────────────────────────────────────────────────────────────────────╯
╭─ Opções ────────────────────────────────────────────────────────────╮
│ --output                TEXT      Diretório de saída                  │
│                                   [padrão: favicons]                  │
│ --manifest/--no-manifest          Gerar um manifesto de aplicativo    │
│                                   web (site.webmanifest)              │
│                                   [padrão: True]                      │
│ --optimize/--no-optimize          Otimizar arquivos PNG usando        │
│                                   Squoosh CLI (requer Node.js e       │
│                                   @squoosh/cli)                       │
│                                   [padrão: False]                     │
│ --webp/--no-webp                  Gerar versões WebP de todos os      │
│                                   ícones                              │
│                                   [padrão: False]                     │
│ --avif/--no-avif                  Gerar versões AVIF de todos os      │
│                                   ícones (requer Pillow com suporte   │
│                                   a AVIF)                             │
│                                   [padrão: False]                     │
│ --app-name              TEXT      Nome do aplicativo para o           │
│                                   manifesto web                       │
│                                   [padrão: My App]                    │
│ --app-short-name        TEXT      Nome curto do aplicativo (padrão:   │
│                                   app_name)                           │
│ --theme-color           TEXT      Cor do tema para o manifesto web    │
│                                   [padrão: #ffffff]                   │
│ --background-color      TEXT      Cor de fundo para o manifesto web   │
│                                   [padrão: #ffffff]                   │
│ --help                            Mostrar esta mensagem e sair.       │
╰───────────────────────────────────────────────────────────────────────╯
```

## 📁 Arquivos Gerados

A ferramenta gera os seguintes arquivos no diretório de saída especificado (padrão: `favicons/`):

```
favicons/
├── android-chrome-192x192.png
├── android-chrome-512x512.png
├── apple-touch-icon.png
├── favicon-16x16.png
├── favicon-32x32.png
├── favicon-48x48.png
├── favicon-96x96.png
├── favicon.ico
├── metadata.html
└── site.webmanifest  (se --manifest for True)
```

**Nota sobre `metadata.html`**: Os caminhos (`href`) no arquivo `metadata.html` são relativos à raiz do seu site (ex: `href="/favicons/favicon.ico"`). Certifique-se de que o diretório de saída (`favicons/` por padrão) esteja acessível a partir da raiz do seu servidor web.

## 🛠️ Desenvolvimento

### Configuração do Ambiente

```bash
# Clone o repositório (se ainda não o fez)
git clone https://github.com/seu-usuario/favicon-generator.git
cd favicon-generator

# Crie e ative um ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# ou: .venv\Scripts\activate    # Windows

# Instale em modo editável com dependências de desenvolvimento
pip install -e '.[dev]'

# Configure os ganchos de pré-commit (opcional, mas recomendado)
pre-commit install
```

### Executando Testes

```bash
pytest
```

### Construindo a Documentação (se MkDocs for usado)

```bash
mkdocs serve
```

## 📜 Licença

Este projeto é licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para enviar um Pull Request. Para mudanças maiores, por favor, abra uma issue primeiro para discutir o que você gostaria de mudar.

---
