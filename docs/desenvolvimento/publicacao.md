# Publicação no PyPI

Este guia explica como publicar uma nova versão do Favicon Generator no PyPI (Python Package Index).

## Pré-requisitos

1. Uma conta no [PyPI](https://pypi.org/account/register/)
2. Uma conta no [TestPyPI](https://test.pypi.org/account/register/) (para testes)
3. `build` e `twine` instalados:
   ```bash
   pip install build twine
   ```
4. Acesso de manutenção ao pacote no PyPI

## Preparação para a Publicação

### 1. Atualize o Número da Versão

Atualize a versão no arquivo `pyproject.toml` seguindo o [Versionamento Semântico](https://semver.org/):

```toml
[project]
version = "1.0.0"  # Atualize conforme necessário
```

### 2. Atualize o CHANGELOG.md

Documente as mudanças na nova versão. Se não existir, crie um:

```bash
touch CHANGELOG.md
```

Exemplo de conteúdo:

```markdown
# Changelog

## [1.0.0] - YYYY-MM-DD

### Adicionado
- Funcionalidade X
- Suporte ao formato Y

### Alterado
- Melhoria na performance de Z

### Corrigido
- Bug #123: Descrição do bug
```

### 3. Atualize o README.md

Certifique-se de que o README.md está atualizado com as últimas mudanças e exemplos.

## Testando a Publicação (Recomendado)

Antes de publicar no PyPI principal, teste no TestPyPI:

### 1. Construa os pacotes

```bash
rm -rf dist/*
python -m build
```

Isso criará arquivos em `dist/`.

### 2. Verifique os pacotes

```bash
twine check dist/*
```

### 3. Faça upload para o TestPyPI

```bash
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

Você precisará das suas credenciais do TestPyPI.

### 4. Teste a instalação

Crie um ambiente virtual limpo e teste a instalação:

```bash
python -m venv test-env
source test-env/bin/activate  # Linux/macOS
# ou test-env\Scripts\activate no Windows

pip install --index-url https://test.pypi.org/simple/ --no-deps favicon-generator
```

## Publicação no PyPI

### 1. Construa os pacotes finais

```bash
rm -rf dist/*
python -m build
```

### 2. Faça upload para o PyPI

```bash
twine upload dist/*
```

Você precisará das suas credenciais do PyPI.

### 3. Verifique a publicação

Visite a página do pacote no PyPI:
```
https://pypi.org/project/favicon-generator/
```

## Pós-Publicação

### 1. Crie uma Release no GitHub

1. Vá para "Releases" no repositório do GitHub
2. Clique em "Draft a new release"
3. Escolha a tag de versão (ex: v1.0.0)
4. Adicione as notas de lançamento (pode copiar do CHANGELOG.md)
5. Faça upload dos arquivos em `dist/` como anexos
6. Publique a release

### 2. Anuncie a Nova Versão

Considere anunciar a nova versão em:
- Fóruns relevantes
- Redes sociais
- Listas de e-mail

## Dicas para uma Boa Publicação

1. **Teste Exaustivamente**: Certifique-se de que todos os testes passam
2. **Documentação Atualizada**: Verifique se a documentação está sincronizada
3. **Versionamento Semântico**: Siga o padrão MAJOR.MINOR.PATCH
4. **Notas de Lançamento Claras**: Documente as mudanças de forma clara
5. **Backup**: Tenha um backup dos arquivos de distribuição

## Solução de Problemas

### Erro de Autenticação

Certifique-se de que você tem um arquivo `~/.pypirc` configurado corretamente:

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = seu-token-aqui

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = seu-token-teste-aqui
```

### Erro de Versão Duplicada

Se encontrar erros de versão duplicada:
1. Incremente o número da versão
2. Reconstrua os pacotes
3. Tente novamente

### Erro de Metadados

Verifique se todos os metadados em `pyproject.toml` estão corretos, especialmente:
- Nome do pacote
- Versão
- Autor
- Descrição
- Classificadores
