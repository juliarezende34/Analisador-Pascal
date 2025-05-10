from LeitorArquivos import LeitorArquivos

from tokenizer import (
    isDelimitador, palavras_reservadas,
    operadores_logicos, io_tokens,
    condicionais, operadores_aritmeticos
)

from ferramentas import lendo_float

from output import write_output, escrever_variavel_ou_numero, caracteres_invalidos

def lexico():
    with open('../output/output.txt', 'w', encoding='utf-8') as f:
        f.write("Código | Item | Linha | Coluna\n")
        f.close()

    Leitor = LeitorArquivos()
    Leitor.LerArquivos()

    arquivo = Leitor.get_lines_program('EXS28.pas')

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

            char_atual = linha[i]
            
            if i > 0:
                ultimo_char = linha[i-1]
            else:
                ultimo_char = ''

            if i + 1 < tamanho_linha:
                proximo_char = linha[i+1]
            else:
                proximo_char = ''
            
            if char_atual in caracteres_invalidos:
                print(f'Caracter inválido: {char_atual} | Linha {cont_linha} | Coluna {cont_coluna}')
                exit(1)

            verificador_float = lendo_float(ultimo_char, char_atual, proximo_char)

            # Tratamento de comentários
            if not aspas_dupla and not aspas_simples:

                if em_comentario:

                    if char_atual == '}':
                        em_comentario = False
                    i += 1
                    cont_coluna += 1
                    continue

                elif char_atual == '{':
                    em_comentario = True
                    i += 1
                    cont_coluna += 1
                    continue

                elif char_atual == '/' and i + 1 < tamanho_linha and linha[i+1] == '/':
                    break  # Pula o resto da linha

            # Se estiver em comentário, ignora o char_atual
            if em_comentario:
                i += 1
                cont_coluna += 1
                continue

            # Tratamento de strings
            if char_atual == '"' and not aspas_simples:
                if aspas_dupla:
                    # Fechamento de string
                    write_output('string', string_buffer, cont_linha, cont_coluna - len(string_buffer) - escape_coluna)
                    escape_coluna = 0
                    string_buffer = ''
                    aspas_dupla = False
                else:
                    # Abertura de string
                    aspas_dupla = True
                i += 1
                cont_coluna += 1
                continue

            elif char_atual == "'" and not aspas_dupla:
                if aspas_simples:
                    # Fechamento de string
                    write_output(
                        'string',
                        string_buffer, cont_linha,
                        cont_coluna - len(string_buffer) - escape_coluna
                    )
                    escape_coluna = 0
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
                if char_atual == '\\':  # chare de escape
                    escape_coluna += 1
                    if i + 1 < tamanho_linha:
                        string_buffer += linha[i+1]
                        i += 2
                        cont_coluna += 2
                        continue
                    else:
                        string_buffer += '\\'
                else:
                    string_buffer += char_atual
                i += 1
                cont_coluna += 1
                continue

            # Tratamento de operadores aninhados
            if (char_atual in [':', '<', '>', '='] or char_atual in operadores_aritmeticos) and operador_aninhado == '':
                operador_aninhado = char_atual
                i += 1
                cont_coluna += 1
                continue
            
            if operador_aninhado:
                if char_atual in ['=', '>']:
                    operador_aninhado += char_atual
                    write_output(
                        'operador',
                        operador_aninhado, cont_linha,
                        cont_coluna - len(operador_aninhado) + 1
                    )
                    if palavra:
                        tam_operador_aninhado = len(operador_aninhado)
                    else:
                        tam_operador_aninhado = 0
                    i += 1
                    cont_coluna += 1
                else:
                    write_output(
                        'operador',
                        operador_aninhado, cont_linha,
                        cont_coluna - len(operador_aninhado)
                    )
                    if palavra:
                        tam_operador_aninhado = len(operador_aninhado)
                    else:
                        tam_operador_aninhado = 0
            
            # Tratamento de delimitadores
            if (isDelimitador(char_atual) or operador_aninhado) and verificador_float is False:
                if palavra:
                    # Processa a palavra acumulada
                    if (palavra in palavras_reservadas) or (palavra in operadores_logicos) or (palavra in io_tokens) or (palavra in condicionais) or (palavra in operadores_aritmeticos):
                        write_output(
                            palavra, palavra,
                            cont_linha, cont_coluna - len(palavra)
                        )
                    else:
                        index_coluna_no_arquivo = cont_coluna - len(palavra) - tam_operador_aninhado
                        escrever_variavel_ou_numero(palavra, cont_linha, index_coluna_no_arquivo)
                        tam_operador_aninhado = 0
                    palavra = ''
                
                if char_atual not in [' ', '\t', '\n'] and isDelimitador(char_atual):  # Ignora espaços em branco
                    write_output(
                        'delimitador',
                        char_atual, cont_linha,
                        cont_coluna
                    )
                if not operador_aninhado:
                    i += 1
                    cont_coluna += 1
                
                operador_aninhado = ''
                continue
                
            # Acumula chares para formar palavras
            palavra += char_atual
            i += 1
            cont_coluna += 1

        # Verificação de caracteres inválidos
        if palavra in caracteres_invalidos:
            print("Erro léxico: caractere inválido: ", palavra)
            exit(1)
        
        # Processa qualquer palavra restante no final da linha (isso porque antes está ignorando os espaços em branco)
        if palavra:
            if palavra in palavras_reservadas or palavra in operadores_logicos or palavra in io_tokens or palavra in condicionais:
                write_output(palavra, palavra, cont_linha, cont_coluna - len(palavra))
            else:
                index_coluna_no_arquivo = cont_coluna - len(palavra) - tam_operador_aninhado
                escrever_variavel_ou_numero(palavra, cont_linha, index_coluna_no_arquivo)
            palavra = ''

        if operador_aninhado:
            write_output('operador', operador_aninhado, cont_linha, cont_coluna-1)
            operador_aninhado = ''

        cont_linha += 1

    # Verificação final
    if aspas_dupla or aspas_simples:
        print("Erro léxico: string não fechada")

    if em_comentario:
        print("Erro léxico: comentário não finalizado")

    print("Resultado da tokenização disponível no arquivo `output.txt`")