# Instalação

## Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes do Python)
- (Opcional) Node.js e npm (para otimização de imagens com Squoosh CLI)

## Instalação via pip (recomendado)

```bash
pip install favicon-generator
```

## Instalação a partir do código-fonte

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/favicon-generator.git
   cd favicon-generator
   ```

2. (Recomendado) Crie e ative um ambiente virtual:

   ```bash
   # Linux/macOS
   python3 -m venv .venv
   source .venv/bin/activate
   
   # Windows
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Instale o pacote:

   ```bash
   pip install .
   ```

   Para desenvolvimento, instale com dependências adicionais:

   ```bash
   pip install -e '.[dev]'
   ```

## Dependências opcionais

Para otimização de imagens com Squoosh CLI:

```bash
npm install -g @squoosh/cli
```

## Verificando a instalação

Verifique se a instalação foi bem-sucedida:

```bash
favicon-generator --version
```

Você deve ver o número da versão instalada.

## Atualizando

Para atualizar uma instalação existente:

```bash
pip install --upgrade favicon-generator
```

## Solução de problemas

### Erro de permissão

Se encontrar erros de permissão ao instalar globalmente, use a flag `--user`:

```bash
pip install --user favicon-generator
```

### Ambiente virtual não ativado

Certifique-se de que o ambiente virtual está ativado antes de instalar o pacote. Você deve ver o nome do ambiente virtual no início do prompt de comando:

```bash
(.venv) seu-usuario@seu-computador:~/favicon-generator$
```
