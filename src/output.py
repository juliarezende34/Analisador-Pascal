from ferramentas import (
    is_hex,
    is_float, is_int,
    is_octal
)

lista_tuplas = []

# Lista de caracteres inválidos
caracteres_invalidos = {'#', '$', '|', '&', '¨', '!', '@', '%', '°', 'º', 'ª', '§', '?', '¹', '²', '³', '£', '¢', '¬', '_'}

dicionario_tokens = {
    ',': 1,
    '.': 2,
    ':': 3,
    '(': 4,
    ')': 5,
    ' ': 6,
    ';': 7,

    '+': 8,
    '-': 9,
    '*': 10,
    '/': 11,

    '=': 12,
    '>': 13,
    '<': 14,
    ':=': 15,
    '==': 16,
    '>=': 17,
    '<=': 18,
    '<>': 19,

    'or': 20,
    'and': 21,
    'not': 22,

    'program': 23,
    'var': 24,
    'integer': 25,
    'float': 26,
    'hexa': 27,
    'octal': 28,
    'real': 29,
    'string': 30,
    'begin': 31,
    'end': 32,
    'for': 33,
    'to': 34,
    'break': 35,
    'mod': 36,
    'div': 37,

    'if': 38,
    'else': 39,
    'then': 40,

    'write': 41,
    'writeln': 42,
    'read': 43,
    'readln': 44,

    '\n': 45,
    '\0': 46,
    'variavel':47
}

def write_output(cod, item, linha, coluna):
    with open('../output/output.txt', 'a', encoding='utf-8') as f:
        if cod == 'string' or cod == 'hexa' or cod == 'octal' or cod == 'float' or cod == 'integer':
            f.write(f"{dicionario_tokens[cod]} | {item} | {linha} | {coluna}\n")
            lista_tuplas.append((dicionario_tokens[cod], item, linha, coluna))
        elif cod == 'variavel':
            if item == 'var':
                f.write(f"{dicionario_tokens['var']} | {item} | {linha} | {coluna}\n")
                lista_tuplas.append((dicionario_tokens['var'], item, linha, coluna))
            else:
                f.write(f"{dicionario_tokens['variavel']} | {item} | {linha} | {coluna}\n")
                lista_tuplas.append((dicionario_tokens['variavel'], item, linha, coluna))
        else:
            f.write(f"{dicionario_tokens[item]} | {item} | {linha} | {coluna}\n")
            lista_tuplas.append((dicionario_tokens[item], item, linha, coluna))
        f.close() 


def escrever_variavel_ou_numero(palavra, cont_linha,  cont_coluna, index_de_saida_no_arquivo):
    if is_hex(palavra, cont_linha, cont_coluna):
        write_output('hexa', palavra, cont_linha, index_de_saida_no_arquivo)
    elif is_int(palavra):
        write_output('integer', palavra, cont_linha, index_de_saida_no_arquivo)
    elif is_octal(palavra):
        write_output('octal', palavra, cont_linha, index_de_saida_no_arquivo)
    elif is_float(palavra, cont_linha, cont_coluna):
        write_output('float', palavra, cont_linha, index_de_saida_no_arquivo)
    else:
        write_output('variavel', palavra, cont_linha, index_de_saida_no_arquivo)