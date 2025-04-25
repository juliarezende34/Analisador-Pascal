from LeitorArquivos import LeitorArquivos
from tokenizer import *
from output import *
from ferramentas import digito_hexadecimal


with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(f"Código | Item{' ' *10} | Linha | Coluna\n")
    f.close()

Leitor = LeitorArquivos()

Leitor.LerArquivos()

arquivos = Leitor.ListaProgramasPascal
palavra = ''
palavra_hexadec = ''
operador_aninhado = ''
delimitador = ''
cod = ''

cont_linha = 1
cont_coluna = 1
hexadecimal_flag = False
last_caracter = ''

# Arquivos com erro ao realizar leitura:
#EXS15.pas -> índice 16 de arquivos

for linha in arquivos[25]:
    #[:527]:                                                               # Lendo a linha
    for caracter in linha:                                                          # Lendo o caracter                          
        # Começo da construção dos caracteres aninhados - //, >=, <=, <>, :=, ==
        if (caracter in [':', '<', '>', '=', '/']) and (operador_aninhado == ''):  
            operador_aninhado = caracter
            continue

        # Se houver os caracteres em sequência, constrói o caracter aninhado
        elif (operador_aninhado != '') and caracter in ['=', '>', '/']:             
            operador_aninhado += caracter
            continue

        # Se não for delimitador ou operador, continua a construir a palavra, letra por letra
        elif not (isDelimitador(caracter) or isOperadorAritmetico(caracter)):
            palavra = palavra + caracter

        # Achou um delimitador e a palavra foi construída
        else:
            # Se '//', é um comentário, então pula pra próxima linha
            if operador_aninhado == '//':
                operador_aninhado = ''
                palavra = ''
                break

            # Se a palavra não está vazia, fazer tratamentos
            if palavra.strip() != '':
                # Printar itens reservados
                if (palavra in operadores_logicos) or (palavra in palavras_reservadas) or (palavra in io_tokens) or (palavra in condicionais):
                    write_output(cod, palavra, cont_linha, cont_coluna)
                # Printar variável
                else:
                    cod = 'variavel'
                    write_output(cod,palavra, cont_linha, cont_coluna)
                    cod = ''
                if operador_aninhado != '':
                    write_output(cod,operador_aninhado, cont_linha, cont_coluna)

                palavra = ''
                operador_aninhado = ''
            write_output(cod, caracter, cont_linha, cont_coluna)
        cont_coluna += 1
    cont_linha += 1
    ultimo_caracter = caracter

print("Resultado da tokenização disponível no arquivo `output.txt`")