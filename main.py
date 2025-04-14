from LeitorArquivos import LeitorArquivos
from tokenizer import isDelimitador, isOperadorAritmetico

Leitor = LeitorArquivos()

Leitor.LerArquivos()

arquivo = Leitor.get_lines_program('EXS1.pas')
palavra = ''
operador_aninhado = ''
delimitador = ''


for linha in arquivo:
    for caracter in linha:
        if (caracter in [':', '<', '>']) and (operador_aninhado == ''):
            operador_aninhado = caracter
            continue
        elif (operador_aninhado != '') and caracter in ['=', '>']:
            operador_aninhado += caracter
            continue
        elif not (isDelimitador(caracter) or isOperadorAritmetico(caracter)):
            palavra = palavra + caracter
        else:
            if palavra.strip() != '':
                print(palavra)

# Aqui teremos que printar no output os delimitadores também
                if operador_aninhado != '':
                    print(f"delimitador aninhado-> '{operador_aninhado}'")
                    operador_aninhado = ''
                else:
                    print(f"delimitador comum-> '{caracter}'")

                palavra = ''

                # """
                # # tratar
                # if not isDelimitador:
                    
                #     # ai pode parar de ler pq o delimitador completo ta aqui, vamos:
                #     # categorizar ele
                #     # apagar a string
                #     # pegar o caracterer atual (que nao faz parte do delimitador) pra nao perder ele]
                #     # volta pro loop normalmente
                # """
