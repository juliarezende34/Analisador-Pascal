from LeitorArquivos import LeitorArquivos
from tokenizer import *
from output import *
<<<<<<< HEAD
from ferramentas import digito_hexadecimal

=======
from erros import *
>>>>>>> 23d87acc87341763823745d68df1d40bca0d8bbd

with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(f"Código | Item | Linha | Coluna\n")
    f.close()

Leitor = LeitorArquivos()

Leitor.LerArquivos()

<<<<<<< HEAD
arquivos = Leitor.ListaProgramasPascal
=======

arquivo = Leitor.get_lines_program('EXS1.pas')

# Variáveis de estado
>>>>>>> 23d87acc87341763823745d68df1d40bca0d8bbd
palavra = ''
palavra_hexadec = ''
operador_aninhado = ''
cod = ''
aspas_dupla = False
aspas_simples = False
string_buffer = ''
cont_linha = 1
cont_coluna = 1
<<<<<<< HEAD
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
=======
em_comentario = False
tam_operador_aninhado = 0
escape_coluna = 0

for linha in arquivo:
    cont_coluna = 1  # Reset a cada nova linha
    i = 0  # Índice para percorrer a linha
    tamanho_linha = len(linha)
    
    while i < tamanho_linha:
        caracter = linha[i]
        
        # Tratamento de comentários
        if not aspas_dupla and not aspas_simples and not em_comentario:
            if caracter == '/' and i + 1 < tamanho_linha and linha[i+1] == '/':
                break  # Pula o resto da linha
            elif caracter == '{':
                em_comentario = True
                i += 1
                continue
            elif caracter == '}' and em_comentario:
                em_comentario = False
                i += 1
                continue
            elif em_comentario:
                i += 1
                continue
        
        # Se estiver em comentário, ignora o caractere
        if em_comentario:
            i += 1
            continue
            
        # Tratamento de strings
        if caracter == '"' and not aspas_simples:
            if aspas_dupla:
                # Fechamento de string
                write_output('string', string_buffer, cont_linha, cont_coluna - len(string_buffer) - escape_coluna)
                escape_coluna=0
                string_buffer = ''
                aspas_dupla = False
            else:
                # Abertura de string
                aspas_dupla = True
            i += 1
            cont_coluna += 1
            continue
            
        elif caracter == "'" and not aspas_dupla:
            if aspas_simples:
                # Fechamento de string
                write_output('string', string_buffer, cont_linha, cont_coluna - len(string_buffer) - escape_coluna)
                escape_coluna=0
                string_buffer = ''
                aspas_simples = False
            else:
                # Abertura de string
                aspas_simples = True
            i += 1
            cont_coluna += 1
            continue
            
        # Se estiver dentro de string (tratamento escape '\')
        if aspas_dupla or aspas_simples:
            if caracter == '\\':  # Caractere de escape
                escape_coluna += 1
                if i + 1 < tamanho_linha:
                    string_buffer += linha[i+1]
                    i += 2
                    cont_coluna += 2
                    continue
>>>>>>> 23d87acc87341763823745d68df1d40bca0d8bbd
                else:
                    string_buffer += '\\'
            else:
                string_buffer += caracter
            i += 1
            cont_coluna += 1
            continue
            
        # Tratamento de operadores aninhados
        if caracter in [':', '<', '>', '=', '/', '*'] and operador_aninhado == '':
            operador_aninhado = caracter
            i += 1
            cont_coluna += 1
            continue
            
        if operador_aninhado:
            if caracter in ['=', '>']:
                operador_aninhado += caracter
                write_output('operador', operador_aninhado, cont_linha, cont_coluna - len(operador_aninhado) + 1)
                if palavra: 
                    tam_operador_aninhado = len(operador_aninhado)
                else:
                    tam_operador_aninhado=0
                operador_aninhado = ''
<<<<<<< HEAD
            write_output(cod, caracter, cont_linha, cont_coluna)
=======
                i += 1
                cont_coluna += 1
                continue
            else:
                write_output('operador', operador_aninhado, cont_linha, cont_coluna - len(operador_aninhado))
                if palavra: 
                    tam_operador_aninhado = len(operador_aninhado)
                else:
                    tam_operador_aninhado=0
                operador_aninhado = ''
                continue
       
        # Tratamento de delimitadores
        if isDelimitador(caracter):
            if palavra:
                # Processa a palavra acumulada
                if (palavra in palavras_reservadas) or (palavra in operadores_logicos) or (palavra in io_tokens) or (palavra in condicionais):
                    write_output(palavra, palavra, cont_linha, cont_coluna - len(palavra))
                else:
                    write_output('variavel', palavra, cont_linha, cont_coluna - len(palavra)- tam_operador_aninhado)
                    tam_operador_aninhado=0
                palavra = ''
            
            if caracter not in [' ', '\t', '\n']:  # Ignora espaços em branco
                write_output('delimitador', caracter, cont_linha, cont_coluna)
            i += 1
            cont_coluna += 1
            continue
            
        # Acumula caracteres para formar palavras
        palavra += caracter
        i += 1
>>>>>>> 23d87acc87341763823745d68df1d40bca0d8bbd
        cont_coluna += 1
    
    # Processa qualquer palavra restante no final da linha (isso porque antes está ignorando os espaços em branco)
    if palavra:
        if palavra in palavras_reservadas or palavra in operadores_logicos or palavra in io_tokens or palavra in condicionais:
            write_output(palavra, palavra, cont_linha, cont_coluna - len(palavra))
        else:
            write_output('variavel', palavra, cont_linha, cont_coluna - len(palavra))
        palavra = ''
    
    if operador_aninhado:
        write_output('operador', operador_aninhado, cont_linha, cont_coluna-1)
        operador_aninhado = ''
    
    cont_linha += 1
    ultimo_caracter = caracter

# Verificação final
if aspas_dupla or aspas_simples:
    print("Erro léxico: string não fechada")
    invalid_token_error()

print("Resultado da tokenização disponível no arquivo `output.txt`")