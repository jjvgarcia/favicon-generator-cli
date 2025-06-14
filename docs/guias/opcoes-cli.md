# Opções da Linha de Comando (CLI)

O Favicon Generator oferece várias opções para personalizar a geração de favicons. Este guia descreve todas as opções disponíveis.

## Visão Geral

```bash
favicon-generator generate [OPÇÕES] IMAGEM
```

## Argumentos

### `IMAGEM` (obrigatório)

Caminho para o arquivo de imagem de origem.

- Deve ser um arquivo de imagem válido (PNG, JPG, SVG, etc.)
- Tamanho recomendado: 512x512 pixels ou maior
- O assunto deve estar centralizado, pois será redimensionado para formatos quadrados

## Opções Principais

### `-o, --output-dir`

Diretório de saída para os arquivos gerados.

- **Padrão**: `favicons`
- **Exemplo**:
  ```bash
  favicon-generator generate logo.png --output-dir static/favicons
  ```

### `--manifest/--no-manifest`

Controla se o manifesto do aplicativo da web (`site.webmanifest`) deve ser gerado.

- **Padrão**: `--manifest` (gerar manifesto)
- **Exemplo para desativar**:
  ```bash
  favicon-generator generate logo.png --no-manifest
  ```

### `--optimize/--no-optimize`

Ativa/desativa a otimização de imagens usando o Squoosh CLI.

- **Requer**: Node.js e `@squoosh/cli` instalado globalmente
- **Padrão**: `--no-optimize`
- **Exemplo**:
  ```bash
  favicon-generator generate logo.png --optimize
  ```

## Formatos de Saída

### `--webp/--no-webp`

Gera versões WebP dos ícones.

- **Padrão**: `--no-webp`
- **Exemplo**:
  ```bash
  favicon-generator generate logo.png --webp
  ```

### `--avif/--no-avif`

Gera versões AVIF dos ícones (requer suporte a AVIF no Pillow).

- **Padrão**: `--no-avif`
- **Exemplo**:
  ```bash
  favicon-generator generate logo.png --avif
  ```

## Personalização do Manifesto

### `--app-name`

Nome do aplicativo para o manifesto da web.

- **Padrão**: `My App`
- **Exemplo**:
  ```bash
  favicon-generator generate logo.png --app-name "Meu Aplicativo"
  ```

### `--app-short-name`

Nome curto do aplicativo (usado quando o espaço é limitado).

- **Padrão**: Igual a `--app-name`
- **Exemplo**:
  ```bash
  favicon-generator generate logo.png --app-name "Meu Aplicativo Incrível" --app-short-name "MeuApp"
  ```

### `--theme-color`

Cor do tema para o manifesto da web.

- **Padrão**: `#ffffff` (branco)
- **Formato**: Código hexadecimal (#RRGGBB)
- **Exemplo**:
  ```bash
  favicon-generator generate logo.png --theme-color "#4f46e5"
  ```

### `--background-color`

Cor de fundo para o manifesto da web.

- **Padrão**: `#ffffff` (branco)
- **Formato**: Código hexadecimal (#RRGGBB)
- **Exemplo**:
  ```bash
  favicon-generator generate logo.png --background-color "#f9fafb"
  ```

## Exemplos de Uso

### Exemplo 1: Configuração básica

```bash
favicon-generator generate logo.png
```

### Exemplo 2: Com otimização e formatos adicionais

```bash
favicon-generator generate logo.png \
  --optimize \
  --webp \
  --avif \
  --output-dir public/favicons
```

### Exemplo 3: Personalização completa

```bash
favicon-generator generate logo.png \
  --app-name "Meu Aplicativo" \
  --app-short-name "MeuApp" \
  --theme-color "#4f46e5" \
  --background-color "#f9fafb" \
  --output-dir static/favicons \
  --optimize
```

## Solução de Problemas

### Verificando a instalação

Verifique se o comando está disponível:

```bash
favicon-generator --version
```

### Erro de formato não suportado

Certifique-se de que a imagem de entrada está em um formato suportado (PNG, JPG, SVG, etc.).

### Problemas com otimização

Se estiver usando `--optimize`, verifique se o Squoosh CLI está instalado:

```bash
squoosh-cli --version
```

Se não estiver instalado:

```bash
npm install -g @squoosh/cli
```

### Mensagens de aviso

- **Imagem muito pequena**: Recomenda-se usar imagens de pelo menos 512x512 pixels
- **Imagem não quadrada**: A imagem será cortada para um quadrado
- **Formato não suportado**: Alguns recursos podem não estar disponíveis para todos os formatos de imagem
