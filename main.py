from tokenizer import *
from sys import argv

#Lê todos os arquivos passados e retrona todos eles em uma única string
def file_reader():
    try:
        file = open(argv[1], 'r')

    except:
        print("Problemas na leitura de arquivos <- main.py")
        exit(1)

    return file
    
arquivo = file_reader()
print(dict_tokens)