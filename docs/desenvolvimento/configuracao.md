# Configuração do Ambiente de Desenvolvimento

Este guia explica como configurar o ambiente de desenvolvimento para contribuir com o Favicon Generator.

## Pré-requisitos

- Python 3.8 ou superior
- Git
- (Opcional) Node.js e npm (para testes de otimização)

## Passo 1: Clonar o repositório

```bash
git clone https://github.com/seu-usuario/favicon-generator.git
cd favicon-generator
```

## Passo 2: Configurar ambiente virtual

Recomenda-se o uso de um ambiente virtual para isolar as dependências do projeto:

```bash
# Criar ambiente virtual
python -m venv .venv

# Ativar ambiente virtual
# Linux/macOS:
source .venv/bin/activate
# Windows:
.venv\Scripts\activate
```

## Passo 3: Instalar dependências

Instale o pacote em modo de desenvolvimento com todas as dependências necessárias:

```bash
pip install -e '.[dev,docs]'
```

Isso instalará:
- O próprio pacote em modo editável
- Dependências de desenvolvimento (testes, formatação, etc.)
- Dependências de documentação

## Passo 4: Configurar pré-commit

O projeto usa pre-commit para executar verificações automáticas antes de cada commit:

```bash
pre-commit install
```

Isso garantirá que seu código siga os padrões antes de cada commit.

## Estrutura do Projeto

```
favicon-generator/
├── favicon_generator/     # Código-fonte do pacote
│   ├── __init__.py
│   ├── cli.py            # Interface de linha de comando
│   ├── generator.py      # Lógica principal de geração
│   ├── metadata.py       # Geração de metadados HTML
│   ├── optimizer.py      # Otimização de imagens
│   └── utils.py          # Funções auxiliares
├── tests/                # Testes automatizados
├── docs/                 # Documentação
├── .pre-commit-config.yaml
├── pyproject.toml        # Configuração do projeto
└── README.md
```

## Ferramentas de Desenvolvimento

### Formatação de Código

O projeto usa Black para formatação automática:

```bash
black .
```

### Verificação de Tipos

O projeto usa mypy para verificação de tipos estáticos:

```bash
mypy favicon_generator
```

### Linting

O projeto usa flake8 para verificação de estilo:

```bash
flake8 favicon_generator
```

### Ordenação de Imports

O projeto usa isort para organizar os imports:

```bash
isort favicon_generator
```

## Configuração do Editor

### VS Code

Recomenda-se as seguintes extensões:

- Python (Microsoft)
- Pylance
- Black Formatter
- isort
- flake8
- mypy

Adicione ao seu `.vscode/settings.json`:

```json
{
    "python.formatting.provider": "black",
    "python.formatting.blackArgs": ["--line-length", "88"],
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "python.linting.mypyEnabled": true,
    "python.linting.pylintEnabled": false,
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
        "source.organizeImports": true
    },
    "python.analysis.typeCheckingMode": "basic"
}
```

## Dicas de Desenvolvimento

1. Sempre crie um branch para suas alterações:
   ```bash
   git checkout -b minha-feature
   ```

2. Execute os testes antes de fazer commit:
   ```bash
   pytest
   ```

3. Atualize a documentação quando necessário

4. Faça commits atômicos com mensagens claras

5. Envie um Pull Request quando sua funcionalidade estiver pronta
