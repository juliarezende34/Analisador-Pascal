# Analisador-Pascal

## Descrição do Projeto
O projeto se propõe à construir um Interpretador da linguagem Pascal([Especificações](https://github.com/juliarezende34/Analisador-Pascal/blob/main/Especifica%C3%A7%C3%B5es/Analisador_L%C3%A9xico.pdf)). Acompanhe o status do projeto abaixo:
[ ] - Análise Léxica
[ ] - Análise Sintática
[ ] - Análise Semântica
[ ] - Interpretação e execução

## Execução de Código

Para rodar o programa siga as instruções:
1. Escreva o nome de variável de ambiente que chama o seu interpretador.
2. Logo em seguida, escreva o nome do programa principal, neste caso main.py.
3. Em posterióri, digite o nome do diretório que contém os arquivos de entrada.

```powershell
py .\main.py .\inputs
```

## Documentação de Código
O código escrito segue padrões de documentação estabelecidos peas PEPs[PEPs]. Desta forma o linter Flake8[#FK8] assistiu o desenvolvimento do projeto.

## PEPs
Em função de garantir uma consistência estilística ao se escrever um código, elaboraram-se as PEPs(Python Enhancement Proposals). À priori, as PEPs propõem que a comunidade escreva seu código seguindo determinados padrões, de modo que qualquer código em Python possa se parecer e ter sua compreensão facilitada. Em síntese, problemas como a falta de caráter declarativo do Python por ser uma linguagem dinâmicamente tipada são resolvidos. Acompanhe o exemplo abaixo para entender melhor:

- PEP 484, PEP 585, PEP 604 e a proposição de Type Hints
```python
def calcular_imposto(valor: float, taxa: float) -> float:
    """Retorna o valor do imposto."""  
    return valor * taxa
 ```
# Referêncial
<!-- PEPs -->[PEPs] https://peps.python.org/#introduction
<!-- Flake8 -->[FK8] - https://flake8.pycqa.org/en/latest/
