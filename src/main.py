from lexico import *
from sintatico import *
 
lista = lexico()

codigo_intermediario = sintatico(lista)

print("\nCódigo Intermediário Gerado:")
for linha in codigo_intermediario:
    print(linha)
