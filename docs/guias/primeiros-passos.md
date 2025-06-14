# Primeiros Passos

Este guia rápido irá ajudá-lo a começar a usar o Favicon Generator para criar seus próprios favicons e ativos para aplicativos da web.

## Pré-requisitos

- Ter o Favicon Generator instalado (veja o [Guia de Instalação](instalacao.md))
- Uma imagem de origem para gerar os favicons (recomendado: 512x512px ou maior, formato PNG ou SVG)

## Passo 1: Preparar sua imagem

Certifique-se de que sua imagem de origem atenda aos seguintes critérios:

- Formato: PNG, JPG, SVG ou qualquer formato suportado pelo Pillow
- Tamanho recomendado: Mínimo 512x512 pixels
- Assunto centralizado: Como ícones são quadrados, o assunto principal deve estar bem centralizado

## Passo 2: Gerar favicons básicos

Execute o seguinte comando para gerar favicons com configurações padrão:

```bash
favicon-generator generate caminho/para/sua/imagem.png
```

Isso criará uma pasta `favicons/` no diretório atual com os seguintes arquivos:

- `favicon.ico` - Ícone tradicional para navegadores antigos
- `favicon-16x16.png` - Ícone 16x16 pixels
- `favicon-32x32.png` - Ícone 32x32 pixels
- `favicon-48x48.png` - Ícone 48x48 pixels
- `favicon-96x96.png` - Ícone 96x96 pixels
- `apple-touch-icon.png` - Ícone para iOS/Android
- `android-chrome-192x192.png` - Ícone para Android Chrome
- `android-chrome-512x512.png` - Ícone para Android Chrome (alta resolução)
- `metadata.html` - Código HTML pronto para copiar e colar
- `site.webmanifest` - Manifesto do aplicativo da web

## Passo 3: Usar os arquivos gerados

### Para sites HTML

1. Copie o conteúdo do arquivo `metadata.html` para a seção `<head>` do seu site.
2. Certifique-se de que a pasta `favicons/` esteja acessível na raiz do seu site.

### Para aplicativos React/Vue/Angular

1. Copie os arquivos gerados para a pasta `public/` do seu projeto.
2. Adicione as tags do `metadata.html` ao componente principal do seu aplicativo.

## Passo 4: Personalização avançada

### Gerar formatos adicionais

```bash
favicon-generator generate caminho/para/sua/imagem.png --webp --avif
```

### Especificar diretório de saída

```bash
favicon-generator generate caminho/para/sua/imagem.png --output-dir public/favicons
```

### Personalizar metadados

```bash
favicon-generator generate caminho/para/sua/imagem.png \
  --app-name "Meu Aplicativo" \
  --theme-color "#4f46e5" \
  --background-color "#ffffff"
```

## Próximos passos

- Consulte o guia [Opções da CLI](opcoes-cli.md) para todas as opções disponíveis
- Aprenda sobre [otimização de imagens](opcoes-cli.md#otimização) para reduzir o tamanho dos arquivos
- Explore a [referência da API](../referencia/modulo.md) para uso programático
