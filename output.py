from tokenizer import *

dicionario_tokens = {
    '\\n': 0,
    '\\t': 0,
    '\\0': 0,
    '': 0,

    ',': 1,
    '.': 1,
    ':': 1,
    '(': 1,
    ')': 1,
    ' ': 1,
    ';': 1,

    '+': 2,
    '-': 2,
    '*': 2,
    '/': 2,

    '=': 3,
    '>': 3,
    '<': 3,
    '==': 3,
    '>=':3,
    '<=': 3,
    '<>': 3,

    'or': 4,
    'and': 4,
    'not': 4,

    'program': 5,
    'var': 5,
    'integer': 5,
    'real': 5,
    'string': 5,
    'begin': 5,
    'end': 5,
    'for': 5,
    'to': 5,
    'break': 5,
    'mod': 5,
    'div': 5,

    'if': 6,
    'else': 6,
    'then': 6,

    'write': 7,
    'writeln': 7,
    'read': 7,
    'readln': 7
}


def write_output(cod, item, linha, coluna):
    with open('output.txt', 'a', encoding='utf-8') as f:
        if cod != 'variavel':
            f.write(f"{dicionario_tokens[item]}{' '*5} | {item}{' ' * (14 - len(item))} | {linha}{' '*(5 - len(str(linha)))} | {coluna}\n")
        else:
            f.write(f"8{' '*5} | {item}{' ' * (14 - len(item))} | {linha}{' '*(5 - len(str(linha)))} | {coluna}\n")
        f.close()