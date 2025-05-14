from LeitorArquivos import LeitorArquivos

from tokenizer import (
    isDelimitador, palavras_reservadas,
    operadores_logicos, io_tokens,
    condicionais, operadores_aritmeticos,
    operadores_comparacao
)

from ferramentas import lendo_float

from output import write_output, escrever_variavel_ou_numero, caracteres_invalidos


def lexico():
    with open('../output/output.txt', 'w', encoding='utf-8') as f:
        f.write("Código | Item | Linha | Coluna\n")
        f.close()

    Leitor = LeitorArquivos()
    Leitor.LerArquivos()

    arquivo = Leitor.get_lines_program('EXS26.pas')

    # Variáveis de estado
    pilha = []  # Para controlar (, [, {
    mapa_delimitadores = {'(': ')'} # {'(': ')', '[': ']', '{': '}'}
    mapa_fechamento = {')': '('} # {')': '(', ']': '[', '}': '{'}

    palavra = ''
    aspas_dupla = False
    aspas_simples = False
    string_buffer = ''
    cont_linha = 1
    cont_coluna = 1
    em_comentario = False
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
                elif char_atual == '{':
                    em_comentario = True
                    i += 1
                    cont_coluna += 1
                elif char_atual == '/' and proximo_char == '/':
                    break  # ignora o restante da linha
                
                # Tratamento de strings
                elif char_atual == '"' and not aspas_simples:
                    aspas_dupla = True
                    i += 1
                    cont_coluna += 1
                elif char_atual == "'" and not aspas_dupla:
                    aspas_simples = True
                    i += 1
                    cont_coluna += 1

                # Tratamento de operadores aninhados
                elif i + 1 < tamanho_linha and char_atual + linha[i+1] in [':=', '<=', '>=', '<>', '==']:
                    if palavra: # Processa qualquer palavra acumulada antes
                        index_coluna_no_arquivo = cont_coluna - len(palavra)
                        escrever_variavel_ou_numero(palavra, cont_linha, cont_coluna - len(palavra), index_coluna_no_arquivo)
                        palavra = ''
                    write_output('operador', char_atual + linha[i+1], cont_linha, cont_coluna)
                    i += 2
                    cont_coluna += 2

                # Tratamento de operadores aritméticos simples
                elif char_atual in operadores_aritmeticos or char_atual in operadores_comparacao:
                    if palavra: # Processa palavra/número antes do operador
                        index_coluna_no_arquivo = cont_coluna - len(palavra)
                        escrever_variavel_ou_numero(palavra, cont_linha, cont_coluna - len(palavra), index_coluna_no_arquivo)
                        palavra = ''
                    write_output('operador', char_atual, cont_linha, cont_coluna)
                    i += 1
                    cont_coluna += 1
                
                # Tratamento de delimitadores
                elif isDelimitador(char_atual) and not verificador_float:
                    if palavra:
                        # Processa a palavra acumulada
                        if palavra in palavras_reservadas or palavra in operadores_logicos or palavra in io_tokens or palavra in condicionais or palavra in operadores_aritmeticos:
                            write_output(palavra, palavra, cont_linha, cont_coluna - len(palavra))
                        else:
                            index_coluna_no_arquivo = cont_coluna - len(palavra)
                            escrever_variavel_ou_numero(palavra, cont_linha, cont_coluna, index_coluna_no_arquivo)
                        palavra = ''

                    # Tratamento de delimitadores com pilha
                    if char_atual in mapa_delimitadores:
                        pilha.append((char_atual, cont_linha, cont_coluna))
                    elif char_atual in mapa_fechamento:
                        if not pilha or pilha[-1][0] != mapa_fechamento[char_atual]:
                            print(f"Erro léxico: delimitador '{char_atual}' sem correspondente na linha {cont_linha}, coluna {cont_coluna}")
                            exit(1)
                        else:
                            pilha.pop()

                    if char_atual not in [' ', '\t', '\n']:
                        write_output('delimitador', char_atual, cont_linha, cont_coluna)

                    i += 1
                    cont_coluna += 1

                # Acumula chares para formar palavras
                else:
                    palavra += char_atual
                    i += 1
                    cont_coluna += 1

            # Se estiver dentro de string (tratamento escape '\')
            elif aspas_dupla or aspas_simples:
                if char_atual == '"' and aspas_dupla:
                    write_output('string', string_buffer, cont_linha, cont_coluna - len(string_buffer) - escape_coluna)
                    string_buffer = ''
                    escape_coluna = 0
                    aspas_dupla = False
                    i += 1
                    cont_coluna += 1
                elif char_atual == "'" and aspas_simples:
                    write_output('string', string_buffer, cont_linha, cont_coluna - len(string_buffer) - escape_coluna)
                    string_buffer = ''
                    escape_coluna = 0
                    aspas_simples = False
                    i += 1
                    cont_coluna += 1
                elif char_atual == '\\': # chare de escape
                    escape_coluna += 1
                    if i + 1 < tamanho_linha:
                        string_buffer += linha[i+1]
                        i += 2
                        cont_coluna += 2
                    else:
                        string_buffer += '\\'
                        i += 1
                        cont_coluna += 1
                else:
                    string_buffer += char_atual
                    i += 1
                    cont_coluna += 1

        # Processa qualquer palavra restante no final da linha (isso porque antes está ignorando os espaços em branco)
        if palavra:
            if palavra in palavras_reservadas or palavra in operadores_logicos or palavra in io_tokens or palavra in condicionais:
                write_output(palavra, palavra, cont_linha, cont_coluna - len(palavra))
            else:
                index_coluna_no_arquivo = cont_coluna - len(palavra)
                escrever_variavel_ou_numero(palavra, cont_linha, cont_coluna, index_coluna_no_arquivo)
            palavra = ''

        cont_linha += 1

    # Verificações finais
    if aspas_dupla or aspas_simples:
        print("Erro léxico: string não fechada")
        exit(1)

    if em_comentario:
        print("Erro léxico: comentário não finalizado")
        exit(1)

    if pilha:
        ultimo_aberto, linha_aberto, coluna_aberto = pilha[-1]
        print(f"Erro léxico: delimitador '{ultimo_aberto}' aberto na linha {linha_aberto}, coluna {coluna_aberto} não foi fechado.")
        exit(1)

    print("Resultado da tokenização disponível no arquivo `output.txt`")
