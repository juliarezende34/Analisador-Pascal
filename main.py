from LeitorArquivos import LeitorArquivos
from tokenizer import *
from output import *
from erros import *

with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(f"Código | Item | Linha | Coluna\n")
    f.close()

Leitor = LeitorArquivos()

Leitor.LerArquivos()


arquivo = Leitor.get_lines_program('EXS1.pas')

# Variáveis de estado
palavra = ''
operador_aninhado = ''
cod = ''
aspas_dupla = False
aspas_simples = False
string_buffer = ''
cont_linha = 1
cont_coluna = 1
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
        if not aspas_dupla and not aspas_simples:

            if em_comentario:

                if caracter == '}':
                    em_comentario = False
                i += 1
                cont_coluna += 1
                continue
            
            elif caracter == '{':
                em_comentario = True
                i += 1
                cont_coluna += 1
                continue
            elif caracter == '/' and i + 1 < tamanho_linha and linha[i+1] == '/':
                break  # Pula o resto da linha

        # Se estiver em comentário, ignora o caractere   
        if em_comentario:
            i += 1
            cont_coluna += 1
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

# Verificação final
if aspas_dupla or aspas_simples:
    print("Erro léxico: string não fechada")
    invalid_token_error()

print("Resultado da tokenização disponível no arquivo `output.txt`")