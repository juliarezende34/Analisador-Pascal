from output import dicionario_tokens

#------------------------------------
# declaracoes de variaveis
#------------------------------------

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

def sintatico(lista):
    print(len(lista))
    consome('program', lista)
    consome('variavel', lista)
    consome(';', lista)
    declarations(lista)
    consome('begin', lista)
    
    if len(lista) == 0:
        print("Análise sintática concluída com sucesso")

    print(len(lista))

#------------------------------------
# instrucoes dos programas
#------------------------------------



#---------------------------
# descricao das instrucoes
#---------------------------

# Comando for
def forStmt(lista):
    consome('for', lista)
    # atrib(lista)
    consome('to', lista)
    endFor(lista)
    consome('do', lista)
    # stmt(lista)

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
    # expr(lista)
    consome('do', lista)
    # stmt(lista)
    
# Comando if
def ifStmt(lista):
    consome('if', lista)
    # expr(lista)
    consome('then', lista)
    # stmt(lista)
    elsePart(lista)

def elsePart(lista):
    if lista[0][0] == dicionario_tokens['else']:
        consome('else', lista)
        # stmt(lista)


#------------------------------
# expressoes
#------------------------------