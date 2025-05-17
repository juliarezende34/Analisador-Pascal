from output import dicionario_tokens
from tokenizer import
{
    io_tokens    
}

#---------------------------------------------------
#       DECLARAÇÕES DAS VARIÁVEIS
#---------------------------------------------------
def consome(codigo, lista):
    if lista[0][0] == dicionario_tokens[codigo]:
        lista.pop(0)
    else:
        print(f"Erro sintático! Esperado: {codigo} | Recebido: {lista[0][1]} | Linha: {lista[0][2]} | Coluna: {lista[0][3]}")
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

def endFor(lista):
    if lista[0][0] == 'IDENT':
        consome('IDENT', lista)
    elif lista[0][0] == 'NUMint':
        consome('NUMint', lista)
    else:
        print(f"Erro sintático! Esperado: integer ou real ou string | Recebido: {lista[0][1]} | Linha: {lista[0][2]} | Coluna: {lista[0][3]}")
        exit(1)



# ---------------------------------------------------
#       INTRUÇÕES DOS PROGRAMAS
# ---------------------------------------------------
# def ioStmt(lista):
#     if lista[0][0] == 'read':
#         consome('read', lista)
#         consome('(', lista)
#         consome('IDENT', lista)
#         consome(')', lista)
#         consome(';', lista)
#     if lista[0][0] in set('write', 'writeln'):
#         consome('read', lista)
#         consome('(', lista)
#         outlist(lista)
#         consome(')', lista)
#         consome(';', lista)
#     if lista[0][0] == 'readln':
#         consome('read', lista)
#         consome('(', lista)
#         consome('IDENT', lista)
#         consome(')', lista)
#         consome(';', lista)

    
def stmt(lista):
    if lista[0][0] in io_tokens:
        # ioStmt(lista)
    elif lista[0][0] == 'while':
        # whileStmt(lista)
    elif lista[0][0] == ':=':
        atrib(lista)
        consome(';', lista)
    elif lista[0][0] == 'if':
        # ifStmt(lista)
    elif lista[0][0] == 'break'
        # break_pascal()
        consome(';', lista)
    elif lista[0][0] == 'continue'
        continue_pascal()
        consome(';', lista)
    else:
        if lista[0][0] == 'begin':
            bloco()
        else:
            consome(';', lista)


def stmtList(lista):
    valor = lista[0][0]

    casos_de_bloco = {'while', 'if', ':=', 'begin', 'break', 'continue'}

    if lista[0][0] in casos_de_bloco:
        stmt(lista)
        stmtList(lista)


def bloco(lista):
    consome('begin', lista)
    stmtList(lista)
    consome('end', lista)
    consome(';', lista)


def sintatico(lista):
    consome('program', lista)
    consome('variavel', lista)
    consome(';', lista)
    declarations(lista)
    consome('begin', lista)
    
    if len(lista) == 0:
        print("Análise sintática concluída com sucesso")
    else:
        bloco(lista)
        
        if len(lista) == 0:
            print("Análise sintática concluída com sucesso")
