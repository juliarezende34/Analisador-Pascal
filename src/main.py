from lexico import *
from sintatico import *
from executarCodigoIntermediario import *
 
lista = lexico()

codigo_intermediario = sintatico(lista)

output_intermediario(codigo_intermediario)

if codigo_intermediario is not None:
   print("\nCódigo intermediário gerado com sucesso! ✔\nResultado disponível no arquivo `codigo_intermediario.txt`.\n\nIniciando execução do código intermediário...\n")


executar_intermediario(codigo_intermediario)

print("\nExecução do código intermediário concluída! ✔\nResultado das variáveis disponível no arquivo `resultado_execucao_intermediario.txt`.\n")