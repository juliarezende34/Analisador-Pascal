from output import dicionario_tokens
from tokenizer import io_tokens    

#---------------------------------------------------
#       DECLARAÇÕES DAS VARIÁVEIS
#---------------------------------------------------
def consome(lexema, lista):
    if lista[0][0] == dicionario_tokens[lexema]:
        lista.pop(0)
    else:
        print(f"Erro sintático! Esperado: {lexema} | Recebido: {lista[0][1]} | Linha: {lista[0][2]} | Coluna: {lista[0][3]}")
        exit(1)

def restoIdentList(lista):
    if lista[0][0] == dicionario_tokens[',']:
        consome(',', lista)
        consome('variavel', lista)
        restoIdentList(lista)

def listaIdent(lista):
    consome('variavel', lista)
    restoIdentList(lista)

def type_function(lista):
    cod = lista[0][0]
    if cod == dicionario_tokens['integer']:
        consome('integer', lista)
    elif cod == dicionario_tokens['real']:
        consome('real', lista)
    elif cod == dicionario_tokens['string']:
        consome('string', lista)
    else:
        print(f"Erro sintático! Esperado: integer ou real ou string | Recebido: {lista[0][1]} | Linha: {lista[0][2]} | Coluna: {lista[0][3]}")
        exit(1)

def declaration(lista):
	listaIdent(lista)
	consome(':', lista)
	type_function(lista)
	consome(';', lista)

def restoDeclaration(lista):
    if lista[0][0] == dicionario_tokens['variavel']:
        declaration(lista)
        restoDeclaration(lista)

def declarations(lista):
    consome('var', lista)
    declaration(lista)
    restoDeclaration(lista)

# ---------------------------------------------------
#       INTRUÇÕES DOS PROGRAMAS
# ---------------------------------------------------
    
def stmt(lista):
    if lista[0][1] in io_tokens:
        ioStmt(lista)
    elif lista[0][0] == dicionario_tokens['for']:
        forStmt(lista)
    elif lista[0][0] == dicionario_tokens['while']:
        whileStmt(lista)
    elif lista[0][0] == dicionario_tokens['variavel']:
        atrib(lista)
        consome(';', lista)
    elif lista[0][0] == dicionario_tokens['if']:
        ifStmt(lista)
    elif lista[0][0] == dicionario_tokens['begin']:
        bloco(lista)
    elif lista[0][0] == dicionario_tokens['break']:
        consome('break', lista)
        consome(';', lista)
    elif lista[0][0] == dicionario_tokens['continue']:
        consome('continue', lista)
        consome(';', lista)
    elif lista[0][0] == dicionario_tokens[';']:
        consome(';', lista)
        


def stmtList(lista):
    casos_de_stmt = {'for', 'read', 'write','readln','writeln','variavel', 'if', 'begin','break','continue',';'}
    cod_casos_de_stmt = {dicionario_tokens[i] for i in casos_de_stmt}
    if lista[0][0] in cod_casos_de_stmt:
        stmt(lista)
        stmtList(lista)


def bloco(lista):
    consome('begin', lista)
    stmtList(lista)
    consome('end', lista)
    consome(';', lista)

#---------------------------
# DESCRIÇÃO DAS INSTRUÇÕES
#---------------------------

# Comando for
def forStmt(lista):
    consome('for', lista)
    atrib(lista)
    consome('to', lista)
    endFor(lista)
    consome('do', lista)
    stmt(lista)

def endFor(lista):  
    if lista[0][0] == dicionario_tokens['variavel']:
        consome('variavel', lista)
    elif lista[0][0] == dicionario_tokens['integer']:
        consome('integer', lista)
    else:
        print(f"Erro sintático: Esperado variável ou número inteiro | Recebido: {lista[0][1]} | Linha: {lista[0][2]} | Coluna: {lista[0][3]}")
        exit(1)

# Comandos de IO
def ioStmt(lista):
    if lista[0][0] == dicionario_tokens['read']:
        consome('read', lista)
        consome('(', lista)
        consome('variavel', lista)
        consome(')', lista)
        consome(';', lista)
    elif lista[0][0] == dicionario_tokens['write']:
        consome('write', lista)
        consome('(', lista)
        outList(lista)
        consome(')', lista)
        consome(';', lista)
    elif lista[0][0] == dicionario_tokens['readln']:
        consome('readln', lista)
        consome('(', lista)
        consome('variavel', lista)
        consome(')', lista)
        consome(';', lista)
    elif lista[0][0] == dicionario_tokens['writeln']:
        consome('writeln', lista)
        consome('(', lista)
        outList(lista)
        consome(')', lista)
        consome(';', lista)
    else:
        print(f"Erro sintático: Esperado comando de IO | Recebido: {lista[0][1]} | Linha: {lista[0][2]} | Coluna: {lista[0][3]}")
        exit(1)

def outList(lista):
    out(lista)
    restoOutList(lista)

def restoOutList(lista):
    if lista[0][0] == dicionario_tokens[',']:
        consome(',', lista)
        outList(lista)

def out(lista):
    if lista[0][0] == dicionario_tokens['string']:
        consome('string', lista)
    elif lista[0][0] == dicionario_tokens['variavel']:
        consome('variavel', lista)
    elif lista[0][0] == dicionario_tokens['integer']:
        consome('integer', lista)
    elif lista[0][0] == dicionario_tokens['float']:
        consome('float', lista)
    else:
        print(f"Erro sintático: Esperado string, variável ou número | Recebido: {lista[0][1]} | Linha: {lista[0][2]} | Coluna: {lista[0][3]}")
        exit(1)

# Comando while
def whileStmt(lista):
    consome('while', lista)
    expr(lista)
    consome('do', lista)
    stmt(lista)
    
# Comando if
def ifStmt(lista):
    consome('if', lista)
    expr(lista)
    consome('then', lista)
    stmt(lista)
    elsePart(lista)

def elsePart(lista):
    if lista[0][0] == dicionario_tokens['else']:
        consome('else', lista)
        stmt(lista)


#------------------------------
# EXPRESSÕES
#------------------------------

def atrib(lista):
    consome('variavel', lista)
    consome(':=', lista)
    expr(lista)

def expr(lista):
    or_function(lista)

def or_function(lista):
    and_function(lista)
    restoOr(lista)

def restoOr(lista):
    if lista[0][0] == dicionario_tokens['or']:
        consome('or',lista)
        and_function(lista)
        restoOr(lista)

def and_function(lista):
    not_function(lista)
    restoAnd(lista)

def restoAnd(lista):
    if lista[0][0] == dicionario_tokens['and']:
        consome('and', lista)
        not_function(lista)
        restoAnd(lista)

def not_function(lista):
    if lista[0][0] == dicionario_tokens['not']:
        consome('not', lista)
        not_function(lista)
    else:
        rel(lista)

def rel(lista):
    add(lista)
    restoRel(lista)

def restoRel(lista):
    if lista[0][0] == dicionario_tokens['==']:
        consome('==', lista)
        add(lista)
    elif lista[0][0] == dicionario_tokens['<>']:
        consome('<>', lista)
        add(lista)
    elif lista[0][0] == dicionario_tokens['<']:
        consome('<', lista)
        add(lista)
    elif lista[0][0] == dicionario_tokens['<=']:
        consome('<=', lista)
        add(lista)
    elif lista[0][0] == dicionario_tokens['>']:
        consome('>', lista)
        add(lista)
    elif lista[0][0] == dicionario_tokens['>=']:
        consome('>=', lista)
        add(lista)

def add(lista):
    mult(lista)
    restoAdd(lista)

def restoAdd(lista):
    if lista[0][0] == dicionario_tokens['+']:
        consome('+', lista)
        mult(lista)
        restoAdd(lista)
    elif lista[0][0] == dicionario_tokens['-']:
        consome('-', lista)
        mult(lista)
        restoAdd(lista)

def mult(lista):
    uno(lista)
    restoMult(lista)

def restoMult(lista):
    if lista[0][0] == dicionario_tokens['*']:
        consome('*', lista)
        uno(lista)
        restoMult(lista)
    elif lista[0][0] == dicionario_tokens['/']:
        consome('/', lista)
        uno(lista)
        restoMult(lista)
    elif lista[0][0] == dicionario_tokens['mod']:
        consome('mod', lista)
        uno(lista)
        restoMult(lista)
    elif lista[0][0] == dicionario_tokens['div']:
        consome('div', lista)
        uno(lista)
        restoMult(lista)

def uno(lista):
    if lista[0][0] == dicionario_tokens['+']:
        consome('+', lista)
        uno(lista)
    elif lista[0][0] == dicionario_tokens['-']:
        consome('-', lista)
        uno(lista)
    else:
        fator(lista)

def fator(lista):
    possibilidades = {'integer','float', 'variavel', '(', 'string', 'hexa', 'octal'}
    cod_possibilidades = {dicionario_tokens[i] for i in possibilidades}

    if lista[0][0] in cod_possibilidades:
        if lista[0][0] == dicionario_tokens['integer']:
            consome('integer', lista)
        elif lista[0][0] == dicionario_tokens['float']:
            consome('float', lista)
        elif lista[0][0] == dicionario_tokens['hexa']:
            consome('hexa', lista)
        elif lista[0][0] == dicionario_tokens['octal']:
            consome('octal', lista)
        elif lista[0][0] == dicionario_tokens['variavel']:
            consome('variavel', lista)
        elif lista[0][0] == dicionario_tokens['(']:
            consome('(', lista)
            expr(lista)
            consome(')', lista)
        elif lista[0][0] == dicionario_tokens['string']:
            consome('string', lista)
    else:
        print(f"Erro sintático: Esperado 'integer','float', 'variavel', '(' ou 'string' | Recebido: {lista[0][1]} | Linha: {lista[0][2]} | Coluna: {lista[0][3]}")
        exit(1)

#------------------------------
# Sintático
#------------------------------

def sintatico(lista):
    consome('program', lista)
    consome('variavel', lista)
    consome(';', lista)
    declarations(lista)
    consome('begin', lista)
    stmtList(lista)
    consome('end', lista)
    consome('.', lista)
    
    if len(lista) == 0:
        print("Análise sintática concluída com sucesso")
