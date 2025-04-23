from tokenizer import *

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
    '==': 15,
    '>=':16,
    '<=': 17,
    '<>': 18,

    'or': 19,
    'and': 20,
    'not': 21,

    'program': 22,
    'var': 23,
    'integer': 24,
    'real': 25,
    'string': 26,
    'begin': 27,
    'end': 28,
    'for': 29,
    'to': 30,
    'break': 31,
    'mod': 32,
    'div': 33,

    'if': 34,
    'else': 35,
    'then': 36,

    'write': 37,
    'writeln': 38,
    'read': 39,
    'readln': 40
}


def write_output(cod, item, linha, coluna):
    with open('output.txt', 'a', encoding='utf-8') as f:
        if cod != 'variavel':
            if item not in [' ', '']:
                f.write(f"{dicionario_tokens[item]}{' '*(6 - len(str(dicionario_tokens[item])))} | {item}{' ' * (14 - len(item))} | {linha}{' '*(5 - len(str(linha)))} | {coluna}\n")
        else:
            f.write(f"8{' '*5} | {item}{' ' * (14 - len(item))} | {linha}{' '*(5 - len(str(linha)))} | {coluna}\n")
        f.close()