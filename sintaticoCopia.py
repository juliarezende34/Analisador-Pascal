from output import dicionario_tokens, tokens_numericos
from tokenizer import io_tokens
from codigoIntermediario import GeradorCodigoIntermediario, ErroSemantico

# Mapeamento inverso
codigo_para_lexema = {v: k for k, v in dicionario_tokens.items()}


# --------------------------------------------------
# FUNÇÕES AUXILIARES
# --------------------------------------------------

def consome(lexema, lista):
    # Consome um token esperado da lista de tokens
    # print(f"Consumindo: {lexema} | Dicionario: {dicionario_tokens[lexema]}")
    if lista[0][0] == dicionario_tokens[lexema]:
        lista.pop(0)
    else:
        print(f"Erro sintático! Esperado: {lexema} | Recebido: {lista[0][1]} | Linha: {lista[0][2]} | Coluna: {lista[0][3]}")
        exit(1)

# --------------------------------------------------
# DECLARAÇÕES DE VARIÁVEIS
# --------------------------------------------------

# Processa lista de variáveis adicionais após vírgula
def restoIdentList(lista):
    nomes = []
    if lista[0][0] == dicionario_tokens[',']:
        consome(',', lista)
        nomes.append(lista[0][1])
        consome('variavel', lista)
        nomes += restoIdentList(lista)
    return nomes

# Processa lista de identificadores na declaração
def listaIdent(lista):
    nomes = [lista[0][1]]
    consome('variavel', lista)
    nomes += restoIdentList(lista)
    return nomes

# Identifica e retorna o tipo da variável
def type_function(lista):
    cod = lista[0][0]
    if cod == dicionario_tokens['integer']:
        consome('integer', lista)
        return 'integer'
    elif cod == dicionario_tokens['real']:
        consome('real', lista)
        return 'real'
    elif cod == dicionario_tokens['string']:
        consome('string', lista)
        return 'string'
    else:
        print(f"Erro sintático! Esperado: integer ou real ou string | Recebido: {lista[0][1]} | Linha: {lista[0][2]} | Coluna: {lista[0][3]}")
        exit(1)

# Processa declaração de variáveis
def declaration(lista, gerador): 
    nomes = listaIdent(lista)
    consome(':', lista)
    tipo = type_function(lista)
    consome(';', lista)
    
    # Gera código para cada variável declarada
    for nome in nomes:
        gerador.gera_declaracao(nome, tipo)

# Processa declarações adicionais
def restoDeclaration(lista, gerador):
    if lista[0][0] == dicionario_tokens['variavel']:
        declaration(lista, gerador)
        restoDeclaration(lista, gerador)

# Processa bloco de declarações VAR
def declarations(lista, gerador):
    consome('var', lista)
    declaration(lista, gerador)
    restoDeclaration(lista, gerador)

# --------------------------------------------------
# INSTRUÇÕES DO PROGRAMA
# --------------------------------------------------

# Processa uma instrução do programa
def stmt(lista, gerador): 
    if lista[0][1] in io_tokens:
        ioStmt(lista, gerador)
    elif lista[0][0] == dicionario_tokens['for']:
        forStmt(lista, gerador)
    elif lista[0][0] == dicionario_tokens['while']:
        whileStmt(lista, gerador)
    elif lista[0][0] == dicionario_tokens['variavel']:
        atrib(lista, gerador)
        consome(';', lista)
    elif lista[0][0] == dicionario_tokens['if']:
        ifStmt(lista, gerador)
    elif lista[0][0] == dicionario_tokens['begin']:
        bloco(lista, gerador)
    elif lista[0][0] == dicionario_tokens['break']:
        consome('break', lista)
        consome(';', lista)
    elif lista[0][0] == dicionario_tokens['continue']:
        consome('continue', lista)
        consome(';', lista)
    elif lista[0][0] == dicionario_tokens[';']:
        consome(';', lista)

# Processa lista de instruções
def stmtList(lista, gerador):
    casos_de_stmt = {'for', 'read', 'write','readln','writeln','variavel', 'if', 'begin','break','continue',';', 'while'}
    cod_casos_de_stmt = {dicionario_tokens[i] for i in casos_de_stmt}
    if lista[0][0] in cod_casos_de_stmt:
        stmt(lista, gerador)
        stmtList(lista, gerador)

# Processa bloco BEGIN...END
def bloco(lista, gerador):
    consome('begin', lista)
    stmtList(lista, gerador)
    consome('end', lista)
    consome(';', lista)

# --------------------------------------------------
# ESTRUTURAS DE CONTROLE
# --------------------------------------------------

# Gera código para loop FOR
def forStmt(lista, gerador):
    label_inicio = gerador.gera_label("FOR")
    label_fim = gerador.gera_label("ENDFOR")
    
    consome('for', lista)
    
    var_controle = lista[0][1]
    atrib(lista, gerador)  # pega o <atrib> da gramática

    gerador.codigo.append(("LABEL", label_inicio, None, None))
    
    consome('to', lista)
    if lista[0][0] == dicionario_tokens['variavel']:
        var_fim = lista[0][1]
        consome('variavel', lista)
    else:
        var_fim = lista[0][1]
        consome('integer', lista)
    
    temp_cond = gerador.gera_temp()
    gerador.gera_operacao('<=', temp_cond, var_controle, var_fim)
    
    consome('do', lista)
    
    gerador.gerar_condicao(temp_cond, label_inicio, label_fim)
    
    # ✅ Chama um único <stmt>
    stmt(lista, gerador)

    temp_inc = gerador.gera_temp()
    gerador.gera_operacao('+', temp_inc, var_controle, 1)
    gerador.gera_atribuicao(var_controle, temp_inc)
    
    gerador.gerar_jump(label_inicio)
    gerador.codigo.append(("LABEL", label_fim, None, None))

# Gera código para loop WHILE
def whileStmt(lista, gerador):
    label_inicio = gerador.gera_label("WHILE")
    label_fim = gerador.gera_label("ENDWHILE")
    
    consome('while', lista)
    gerador.codigo.append(("LABEL", label_inicio, None, None))
    
    condicao = expr(lista, gerador)
    
    consome('do', lista)
    
    gerador.gerar_condicao(condicao, label_inicio, label_fim)
    
    stmt(lista, gerador)  # ✅ um único stmt
    
    gerador.gerar_jump(label_inicio)
    gerador.codigo.append(("LABEL", label_fim, None, None))

# Gera código para condicional IF
def ifStmt(lista, gerador):
    label_else = gerador.gera_label("ELSE")
    label_fim = gerador.gera_label("ENDIF")
    
    consome('if', lista)
    
    condicao = expr(lista, gerador)
    
    consome('then', lista)
    
    gerador.gerar_condicao(condicao, label_else, label_fim)
    
    stmt(lista, gerador)  # ✅ THEN é um único stmt
    
    gerador.gerar_jump(label_fim)
    gerador.codigo.append(("LABEL", label_else, None, None))
    
    elsePart(lista, gerador)
    
    gerador.codigo.append(("LABEL", label_fim, None, None))


# Processa parte ELSE do IF
def elsePart(lista, gerador):
    if lista[0][0] == dicionario_tokens['else']:
        consome('else', lista)
        stmt(lista, gerador) 


# --------------------------------------------------
# ENTRADA/SAÍDA
# --------------------------------------------------

# Processa comandos de entrada/saída
def ioStmt(lista, gerador):
    if lista[0][0] == dicionario_tokens['read'] or lista[0][0] == dicionario_tokens['readln']:
        comando = lista[0][1]
        consome(comando, lista)
        consome('(', lista)
        var = lista[0][1]
        consome('variavel', lista)
        consome(')', lista)
        consome(';', lista)
        
        # Se for readln, adiciona uma quebra de linha após a leitura
        if comando == 'readln':
            gerador.gera_leitura(var, 'integer')
            gerador.gera_escrita("'\\n'")  # Adiciona quebra de linha
        else:
            gerador.gera_leitura(var, 'integer')
            
    elif lista[0][0] == dicionario_tokens['write'] or lista[0][0] == dicionario_tokens['writeln']:
        comando = lista[0][1]
        consome(comando, lista)
        consome('(', lista)
        outList(lista, gerador)
        consome(')', lista)
        consome(';', lista)
        
        # Se for writeln, adiciona uma quebra de linha após a escrita
        if comando == 'writeln':
            gerador.gera_escrita("'\n'")

# Processa lista de saída
def outList(lista, gerador):
    out(lista, gerador)
    restoOutList(lista, gerador)

# Processa itens adicionais na lista de saída#
def restoOutList(lista, gerador):
    if lista[0][0] == dicionario_tokens[',']:
        consome(',', lista)
        outList(lista, gerador)

# Processa um item de saída
def out(lista, gerador):
    if lista[0][0] == dicionario_tokens['string']:
        valor = lista[0][1]
        consome('string', lista)
        gerador.gera_escrita(valor)
    elif lista[0][0] == dicionario_tokens['variavel']:
        var = lista[0][1]
        consome('variavel', lista)
        gerador.gera_escrita(var)
    elif lista[0][0] == dicionario_tokens['integer']:
        valor = lista[0][1]
        consome('integer', lista)
        gerador.gera_escrita(valor)
    elif lista[0][0] == dicionario_tokens['float']:
        valor = lista[0][1]
        consome('float', lista)
        gerador.gera_escrita(valor)
    else:
        print(f"Erro sintático: Esperado string, variável ou número | Recebido: {lista[0][1]} | Linha: {lista[0][2]} | Coluna: {lista[0][3]}")
        exit(1)

# --------------------------------------------------
# EXPRESSÕES
# --------------------------------------------------

# Processa atribuição de variável
def atrib(lista, gerador):
    var = lista[0][1]
    consome('variavel', lista)
    consome(':=', lista)
    
    # Processa expressão completa
    valor = expr(lista, gerador)
    gerador.gera_atribuicao(var, valor)

# Processa expressão lógica OR
def expr(lista, gerador):
    return or_function(lista, gerador)

# Processa operações OR
def or_function(lista, gerador):
    esq = and_function(lista, gerador)
    return restoOr(lista, gerador, esq)

# Processa operações OR adicionais
def restoOr(lista, gerador, esq):
    if lista[0][0] == dicionario_tokens['or']:
        consome('or', lista)
        dir = and_function(lista, gerador)
        temp = gerador.gera_temp()
        gerador.gera_operacao('ou', temp, esq, dir)
        return restoOr(lista, gerador, temp)
    return esq

# Processa operações AND
def and_function(lista, gerador):
    esq = not_function(lista, gerador)
    return restoAnd(lista, gerador, esq)

# Processa operações AND adicionais
def restoAnd(lista, gerador, esq):
    if lista[0][0] == dicionario_tokens['and']:
        consome('and', lista)
        dir = not_function(lista, gerador)
        temp = gerador.gera_temp()
        gerador.gera_operacao('and', temp, esq, dir)
        return restoAnd(lista, gerador, temp)
    return esq

# Processa operador NOT
def not_function(lista, gerador):
    if lista[0][0] == dicionario_tokens['not']:
        consome('not', lista)
        op = not_function(lista, gerador)
        temp = gerador.gera_temp()
        gerador.codigo.append(('NOT', temp, op, None))
        return temp
    return rel(lista, gerador)

# Processa relações comparativas
def rel(lista, gerador):
    esq = add(lista, gerador)
    return restoRel(lista, gerador, esq)

# Processa operadores relacionais com conversão para códigos de 3 letras
def restoRel(lista, gerador, esq):
    OP_MAP = {
        '<=': 'LEQ',
        '<': 'LESS',
        '>=': 'GEQ',
        '>': 'GRET',
        '==': 'EQ',
        '<>': 'NEQ',
        '=': 'EQ',
    }
    
    if lista[0][0] in [dicionario_tokens['=='], dicionario_tokens['<>'],
                       dicionario_tokens['<'], dicionario_tokens['<='],
                       dicionario_tokens['>'], dicionario_tokens['>=']]:
        op_simbolo = lista[0][1]  # Pega o símbolo do operador (como '<=')
        op_code = OP_MAP[op_simbolo]  # Converte para 'LEQ'
        consome(op_simbolo, lista)
        dir = add(lista, gerador)
        temp = gerador.gera_temp()
        
        # Adiciona diretamente com o código convertido
        gerador.codigo.append((op_code, temp, esq, dir))
        return temp
    return esq

# Processa adições e subtrações
def add(lista, gerador):
    esq = mult(lista, gerador)
    return restoAdd(lista, gerador, esq)

# Processa operadores aditivos
def restoAdd(lista, gerador, esq):
    if lista[0][0] == dicionario_tokens['+']:
        consome('+', lista)
        dir = mult(lista, gerador)
        temp = gerador.gera_temp()
        gerador.gera_operacao('+', temp, esq, dir)
        return restoAdd(lista, gerador, temp)
    elif lista[0][0] == dicionario_tokens['-']:
        consome('-', lista)
        dir = mult(lista, gerador)
        temp = gerador.gera_temp()
        gerador.gera_operacao('-', temp, esq, dir)
        return restoAdd(lista, gerador, temp)
    return esq

# Processa multiplicações e divisões
def mult(lista, gerador):
    esq = uno(lista, gerador)
    return restoMult(lista, gerador, esq)

# Processa operadores multiplicativos
def restoMult(lista, gerador, esq):
    if lista[0][0] == dicionario_tokens['*']:
        consome('*', lista)
        dir = uno(lista, gerador)
        temp = gerador.gera_temp()
        gerador.gera_operacao('*', temp, esq, dir)
        return restoMult(lista, gerador, temp)
    elif lista[0][0] == dicionario_tokens['/']:
        consome('/', lista)
        dir = uno(lista, gerador)
        temp = gerador.gera_temp()
        gerador.gera_operacao('/', temp, esq, dir)
        return restoMult(lista, gerador, temp)
    elif lista[0][0] == dicionario_tokens['mod']:
        consome('mod', lista)
        dir = uno(lista, gerador)
        temp = gerador.gera_temp()
        gerador.gera_operacao('%', temp, esq, dir)
        return restoMult(lista, gerador, temp)
    elif lista[0][0] == dicionario_tokens['div']:
        consome('div', lista)
        dir = uno(lista, gerador)
        temp = gerador.gera_temp()
        gerador.gera_operacao('#', temp, esq, dir)
        return restoMult(lista, gerador, temp)
    return esq

# Processa operadores unários
def uno(lista, gerador):
    if lista[0][0] == dicionario_tokens['+']:
        consome('+', lista)
        return uno(lista, gerador)
    elif lista[0][0] == dicionario_tokens['-']:
        consome('-', lista)
        op = uno(lista, gerador)
        temp = gerador.gera_temp()
        gerador.gera_operacao('not', temp, op, None)
        return temp
    return fator(lista, gerador)

# # Processa fatores primários
# def fator(lista, gerador):
#     if lista[0][0] == dicionario_tokens['integer']:
#         valor = lista[0][1]
#         consome('integer', lista)
#         return valor
#     elif lista[0][0] == dicionario_tokens['float']:
#         valor = lista[0][1]
#         consome('float', lista)
#         return valor
#     elif lista[0][0] == dicionario_tokens['variavel']:
#         var = lista[0][1]
#         consome('variavel', lista)
#         return var
#     elif lista[0][0] == dicionario_tokens['(']:
#         consome('(', lista)
#         res = expr(lista, gerador)
#         consome(')', lista)
#         return res
#     else:
#         print(f"Erro sintático: Fator inválido | Recebido: {lista[0][1]} | Linha: {lista[0][2]} | Coluna: {lista[0][3]}")
#         exit(1)

def fator(lista, gerador):
    if lista[0][0] in tokens_numericos:
        valor = lista[0][1]
        consome(codigo_para_lexema[lista[0][0]], lista)
        return valor
    elif lista[0][0] == dicionario_tokens['variavel']:
        var = lista[0][1]
        consome('variavel', lista)
        return var
    elif lista[0][0] == dicionario_tokens['(']:
        consome('(', lista)
        res = expr(lista, gerador)
        consome(')', lista)
        return res
    else:
        print(f"Erro sintático: Fator inválido | Recebido: {lista[0][1]} | Linha: {lista[0][2]} | Coluna: {lista[0][3]}")
        exit(1)


# --------------------------------------------------
# FUNÇÃO PRINCIPAL
# --------------------------------------------------

# Função principal do analisador sintático
def sintatico(lista_tokens):
    gerador = GeradorCodigoIntermediario()
    
    # Cabeçalho do programa
    consome('program', lista_tokens)
    consome('variavel', lista_tokens)
    consome(';', lista_tokens)
    
    # Declarações de variáveis
    declarations(lista_tokens, gerador)
    
    # Corpo do programa
    consome('begin', lista_tokens)
    stmtList(lista_tokens, gerador)
    consome('end', lista_tokens)
    consome('.', lista_tokens)
    
    # Verifica se todos os tokens foram processados
    if len(lista_tokens) > 0:
        print(f"Erro sintático: Tokens não processados: {lista_tokens[0][1]}")
        exit(1)
    
    return gerador.get_codigo()