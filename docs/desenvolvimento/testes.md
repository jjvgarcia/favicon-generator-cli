# Testes

Este guia cobre como executar e escrever testes para o Favicon Generator.

## Executando Testes

### Executar todos os testes

```bash
pytest
```

### Executar testes com cobertura

```bash
pytest --cov=favicon_generator --cov-report=term-missing
```

### Executar testes específicos

```bash
# Por caminho de arquivo
pytest tests/test_generator.py

# Por nome de teste
pytest -k "test_generate_favicons"

# Com saída detalhada
pytest -v
```

## Estrutura de Testes

Os testes estão organizados no diretório `tests/`:

```
tests/
├── __init__.py
├── conftest.py      # Configurações e fixtures comuns
├── test_generator.py
└── test_metadata.py
```

## Fixtures

O projeto inclui fixtures úteis em `conftest.py`:

### `temp_dir`

Cria um diretório temporário para testes.

### `sample_image`

Fornece uma imagem de teste 512x512 pixels.

### `sample_svg`

Fornece um SVG de teste.

## Escrevendo Testes

### Exemplo Básico

```python
def test_generate_favicons(temp_dir, sample_image):
    """Testa a geração de favicons a partir de uma imagem."""
    from favicon_generator.generator import generate_favicons
    
    # Executa a função sendo testada
    result = generate_favicons(
        image_path=sample_image,
        output_dir=temp_dir
    )
    
    # Verifica se os arquivos foram criados
    expected_files = [
        'favicon.ico',
        'favicon-16x16.png',
        'favicon-32x32.png',
        'metadata.html',
        'site.webmanifest'
    ]
    
    for filename in expected_files:
        assert (temp_dir / filename).exists()
        assert str(temp_dir / filename) in result.values()
```

### Testando Exceções

```python
import pytest

def test_invalid_image(temp_dir):
    """Testa o tratamento de imagem inválida."""
    from favicon_generator.generator import generate_favicons
    from favicon_generator.exceptions import InvalidImageError
    
    with pytest.raises(InvalidImageError):
        generate_favicons(
            image_path="arquivo_inexistente.png",
            output_dir=temp_dir
        )
```

### Testes com Mock

Para testar interações externas (como chamadas ao Squoosh CLI):

```python
from unittest.mock import patch

def test_optimization(temp_dir, sample_image):
    """Testa a otimização de imagens."""
    from favicon_generator.optimizer import optimize_image
    
    with patch('subprocess.run') as mock_run:
        # Configura o mock para retornar com sucesso
        mock_run.return_value.returncode = 0
        
        # Chama a função com otimização ativada
        result = optimize_image(sample_image, temp_dir / "optimized.png")
        
        # Verifica se o comando foi chamado corretamente
        mock_run.assert_called_once()
        assert result == str(temp_dir / "optimized.png")
```

## Testes de Integração

Para testar a integração entre módulos:

```python
def test_cli_integration(temp_dir, sample_image, runner):
    """Testa a integração da CLI com o gerador."""
    from favicon_generator.cli import app
    
    # Cria um arquivo temporário para a imagem
    test_image = temp_dir / "test.png"
    test_image.write_bytes(sample_image.read_bytes())
    
    # Executa o comando CLI
    result = runner.invoke(
        app,
        ["generate", str(test_image), "--output-dir", str(temp_dir)]
    )
    
    # Verifica o resultado
    assert result.exit_code == 0
    assert (temp_dir / "favicon.ico").exists()
```

## Boas Práticas

1. **Nomes Descritivos**: Use nomes descritivos para as funções de teste
2. **Teste um Aspecto por Vez**: Cada teste deve verificar apenas uma coisa
3. **Use Fixtures**: Reutilize configurações comuns usando fixtures
4. **Mocke Dependências Externas**: Isole testes de serviços externos
5. **Teste Casos de Erro**: Verifique como o código lida com entradas inválidas

## Cobertura de Código

Para verificar a cobertura de testes:

```bash
pytest --cov=favicon_generator --cov-report=html
```

Isso gerará um relatório HTML em `htmlcov/` mostrando quais partes do código estão cobertas por testes.

## Testes em CI

O projeto inclui um workflow de CI que executa:

1. Testes unitários
2. Verificação de tipos
3. Verificação de estilo
4. Geração de documentação

Certifique-se de que todos os testes passem antes de enviar um Pull Request.
