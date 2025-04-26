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
    ':=': 15,
    '==': 16,
<<<<<<< HEAD
    '>=':17,
=======
    '>=': 17,
>>>>>>> 23d87acc87341763823745d68df1d40bca0d8bbd
    '<=': 18,
    '<>': 19,

    'or': 20,
    'and': 21,
    'not': 22,

    'program': 23,
    'var': 24,
    'integer': 25,
    'real': 26,
    'string': 27,
    'begin': 28,
<<<<<<< HEAD
    'end': 29,
=======
    'end': 20,
>>>>>>> 23d87acc87341763823745d68df1d40bca0d8bbd
    'for': 30,
    'to': 31,
    'break': 32,
    'mod': 33,
    'div': 34,

    'if': 35,
    'else': 36,
    'then': 37,

    'write': 38,
    'writeln': 39,
    'read': 40,
<<<<<<< HEAD
    'readln': 41,

    '\n': 42,
    '\0': 43
=======
    'readln': 41
>>>>>>> 23d87acc87341763823745d68df1d40bca0d8bbd
}


def write_output(cod, item, linha, coluna):
    with open('output.txt', 'a', encoding='utf-8') as f:
<<<<<<< HEAD
        if item == '\n' or item == '\0' or item == 'b\n' or item == 'b':
            f.write(f"{dicionario_tokens[item]}{' '*(6 - len(str(dicionario_tokens[item])))} | exception case{' ' * (1 - len(item))} | {linha}{' '*(5 - len(str(linha)))} | {coluna}\n")
            return
        if cod != 'variavel':
            if item not in [' ', '']:
                f.write(f"{dicionario_tokens[item]}{' '*(6 - len(str(dicionario_tokens[item])))} | {item}{' ' * (14 - len(item))} | {linha}{' '*(5 - len(str(linha)))} | {coluna}\n")
        else:
            f.write(f"8{' '*5} | {item}{' ' * (14 - len(item))} | {linha}{' '*(5 - len(str(linha)))} | {coluna}\n")
        f.close()
    # with open('output.txt', 'a', encoding='utf-8') as f:
    #     if cod == 'string':
    #         f.write(f"\t{dicionario_tokens[cod]} - {item} - {linha} - {coluna - len(item)}\t\n")
    #     elif cod == 'variavel':
    #         f.write(f"\t{dicionario_tokens['var']} - {item} - {linha} - {coluna - len(item)}\t\n")
    #     else:
    #         if item == '\n' or item == '\0':
    #             f.write(f"\t{dicionario_tokens[item]} - {item.encode()} - {linha} - {coluna}\t\n")

    #         f.write(f"\t{dicionario_tokens[item]} - {item} - {linha} - {coluna - len(item)}\t\n")
            
            
    #     f.close()
=======
        if cod == 'string':  
            f.write(f"{dicionario_tokens[cod]} | {item} | {linha} | {coluna}\n")
        elif cod == 'variavel':
            f.write(f"{dicionario_tokens['var']} | {item} | {linha} | {coluna}\n")
        else:
            f.write(f"{dicionario_tokens[item]} | {item} | {linha} | {coluna}\n")
        f.close()
>>>>>>> 23d87acc87341763823745d68df1d40bca0d8bbd

