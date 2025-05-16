from output import dicionario_tokens

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
    consome('program', lista)
    consome('variavel', lista)
    consome(';', lista)
    declarations(lista)
    consome('begin', lista)
    
    if len(lista) == 0:
        print("Análise sintática concluída com sucesso")