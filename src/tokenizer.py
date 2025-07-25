delimitadores ={',', '.', ':', '(', ')', ' ', ';', '\n', '\t', '\0'}

delimitadoresSalvar ={',', '.', ':', '(', ')', ';', '\n', '\t', '\0', '*'}

operadores_aritmeticos ={'+', '-', '*', '/'}

operadores_comparacao ={'=', '>', '<'}

operadores_logicos ={'or', 'and', 'not'}

palavras_reservadas ={
    'program', 'var', 'integer', 'real', 'string',
    'begin', 'end', 'for', 'to', 'break', 'mod', 'div', 'while','do', 'continue',
}

condicionais ={'if', 'else', 'then'}

io_tokens = {'write', 'writeln', 'read', 'readln'}

# Mapeamento completo de operadores para código intermediário
mapeamento_operadores = {
    # Operadores relacionais
    '<=': 'LEQ',
    '<': 'LESS',
    '>=': 'GEQ',
    '>': 'GRET',
    '==': 'EQ',
    '<>': 'NEQ',
    '=': 'EQ',
    
    # Operadores aritméticos
    '+': 'ADD',
    '-': 'SUB',
    '*': 'MULT',
    '/': 'FDIV',  
    'div': 'IDIV', 
    'mod': 'MOD',
    
    # Operadores lógicos
    'and': 'AND',
    'or': 'OR',
    'not': 'NOT'
}

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