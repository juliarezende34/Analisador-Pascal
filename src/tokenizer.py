delimitadores ={',', '.', ':', '(', ')', ' ', ';', '\n', '\t', '\0'}

delimitadoresSalvar ={',', '.', ':', '(', ')', ';', '\n', '\t', '\0', '*'}

operadores_aritmeticos ={'+', '-', '*', '/'}

operadores_comparacao ={'=', '>', '<'}

operadores_logicos ={'or', 'and', 'not'}

palavras_reservadas ={
    'program', 'var', 'integer', 'real', 'string',
    'begin', 'end', 'for', 'to', 'break', 'mod', 'div'
}

condicionais ={'if', 'else', 'then'}

io_tokens = {'write', 'writeln', 'read', 'readln'}


def isDelimitador(token):
    return token in delimitadores


def isOperadorAritmetico(token):
    return token in operadores_aritmeticos


def isOperadorLogico(token):
    return token in operadores_logicos


def isOperadorComparacao(token):
    return token in operadores_comparacao


def isPalavraReservada(token):
    return token in palavras_reservadas


def isCondicional(token):
    return token in condicionais


def isIO(token):
    return token in io_tokens