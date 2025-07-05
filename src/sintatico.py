from output import dicionario_tokens, tokens_numericos
from tokenizer import io_tokens
from codigoIntermediario import GeradorCodigoIntermediario, ErroSemantico

# Mapeamento inverso
codigo_para_lexema = {v: k for k, v in dicionario_tokens.items()}

dict_tipos = {}

# --------------------------------------------------
# FUNÇÕES AUXILIARES
# --------------------------------------------------

def tipo_valor(valor):
    # Se for variável declarada
    if valor in dict_tipos.keys():
        return dict_tipos[valor]
    elif type(valor) == type(2):
        return 'integer'
    elif type(valor) == type(2.5):
        return 'real'
    elif type(valor) == type('text'):
        return 'string'


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
        dict_tipos[nome] = tipo  # Armazena o tipo da variável no dicionário
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

# ---------------------------------------------------
#       INTRUÇÕES DOS PROGRAMAS
# ---------------------------------------------------
    
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
        if not gerador.pilha_break:
            raise ErroSemantico("Uso de 'break' fora de laço")
        gerador.gerar_jump(gerador.pilha_break[-1])
    elif lista[0][0] == dicionario_tokens['continue']:
        consome('continue', lista)
        consome(';', lista)
        if not gerador.pilha_continue:
            raise ErroSemantico("Uso de 'continue' fora de laço")
        gerador.gerar_jump(gerador.pilha_continue[-1])
    elif lista[0][0] == dicionario_tokens[';']:
        consome(';', lista)

def stmtList(lista, gerador):
    casos_de_stmt = {'for', 'read', 'write', 'readln', 'writeln', 'variavel', 'if', 'begin', 'break', 'continue', ';', 'while'}
    cod_casos_de_stmt = {dicionario_tokens[i] for i in casos_de_stmt}
    
    while lista and lista[0][0] in cod_casos_de_stmt:
        stmt(lista, gerador)

# Processa bloco BEGIN...END
def bloco(lista, gerador):
    consome('begin', lista)
    stmtList(lista, gerador)
    consome('end', lista)
    consome(';', lista)

#---------------------------
# DESCRIÇÃO DAS INSTRUÇÕES
#---------------------------

# Comando for
def forStmt(lista, gerador):
    consome('for', lista)
    var_controle = lista[0][1]
    consome('variavel', lista)
    consome(':=', lista)
    valor_inicio = expr(lista, gerador)

    consome('to', lista)
    valor_fim = expr(lista, gerador)

    consome('do', lista)

    def corpo_for(label_continue, label_end):
        if lista[0][0] == dicionario_tokens['begin']:
            bloco(lista, gerador)
        else:
            stmt(lista, gerador)

    gerador.gerar_for(var_controle, valor_inicio, valor_fim, corpo_for)


def endFor(lista): 
    if lista[0][0] == dicionario_tokens['variavel']:
        valor = lista[0][1]
        consome('variavel', lista)
        return valor
    elif lista[0][0] == dicionario_tokens['integer']:
        valor = lista[0][1]
        consome('integer', lista)
        return valor
    else:
        print(f"Erro sintático: Esperado variável ou número inteiro | Recebido: {lista[0][1]} | Linha: {lista[0][2]} | Coluna: {lista[0][3]}")
        exit(1)

# Comando while
def whileStmt(lista, gerador):
    label_inicio = gerador.gera_label("WHILE")
    label_fim = gerador.gera_label("ENDWHILE")

    # Configura pilhas para break/continue
    gerador.pilha_break.append(label_fim)
    gerador.pilha_continue.append(label_inicio)

    consome('while', lista)
    
    # Início do loop
    gerador.codigo.append(("LABEL", label_inicio, None, None))

    # Condição
    condicao = expr(lista, gerador)
    gerador.gerar_condicao(condicao, None, label_fim)  # Se falso, sai do loop

    consome('do', lista)
    stmt(lista, gerador)  # Corpo do while

    # Volta para verificação
    gerador.gerar_jump(label_inicio)

    # Fim do loop
    gerador.codigo.append(("LABEL", label_fim, None, None))

    # Remove das pilhas
    gerador.pilha_break.pop()
    gerador.pilha_continue.pop()

    
# Comando if
def ifStmt(lista, gerador):
    label_else = gerador.gera_label("ELSE")

    consome('if', lista)
    condicao = expr(lista, gerador)
    consome('then', lista)

    # Se condição falsa, pula para else
    gerador.gerar_condicao(condicao, None, label_else)

    # Bloco then
    stmt(lista, gerador)

    # Verifica se há else
    if lista[0][0] == dicionario_tokens['else']:
        label_fim = gerador.gera_label("ENDIF")
        gerador.gerar_jump(label_fim)
        gerador.codigo.append(("LABEL", label_else, None, None))
        consome('else', lista)
        stmt(lista, gerador)
        gerador.codigo.append(("LABEL", label_fim, None, None))
    else:
        gerador.codigo.append(("LABEL", label_else, None, None))


def elsePart(lista, gerador):
    if lista[0][0] == dicionario_tokens['else']:
        consome('else', lista)
        stmt(lista, gerador)


# --------------------------------------------------
# ENTRADA/SAÍDA
# --------------------------------------------------

# Comandos de IO
def ioStmt(lista, gerador):
    if lista[0][0] == dicionario_tokens['read'] or lista[0][0] == dicionario_tokens['readln']:
        comando = lista[0][1]
        consome(comando, lista)
        consome('(', lista)
        var = lista[0][1]
        consome('variavel', lista)
        consome(')', lista)
        consome(';', lista)
        # Não gera mais PRINT '\n' após readln
        gerador.gera_leitura(var, dict_tipos[var])
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
    else:
        print(f"Erro sintático: Esperado comando de IO | Recebido: {lista[0][1]} | Linha: {lista[0][2]} | Coluna: {lista[0][3]}")
        exit(1)

def outList(lista, gerador):
    out(lista, gerador)
    restoOutList(lista, gerador)

def restoOutList(lista, gerador):
    if lista[0][0] == dicionario_tokens[',']:
        consome(',', lista)
        outList(lista, gerador)

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
#------------------------------
# EXPRESSÕES
#------------------------------

# Processa atribuição de variável
def atrib(lista, gerador):
    var = lista[0][1]

    consome('variavel', lista)
    consome(':=', lista)
    # Processa expressão completa
    valor = expr(lista, gerador)
    if var in dict_tipos.keys():
        gerador.gera_atribuicao(var, valor)
    else:
        raise ErroSemantico(f"Erro: variável {var} utilizada sem inicialização prévia")

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
        gerador.gera_operacao('or', temp, esq, dir)

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

# Processa operadores relacionais com conversão para seus respectivos códigos
def restoRel(lista, gerador, esq):
    OP_MAP = {
        '<=': 'LEQ',
        '<': 'LESS',
        '>=': 'GEQ',
        '>': 'GRET',
        '==': 'EQ',
        '<>': 'NEQ',
        '=': 'EQ',
        ':=': 'ATT'
    }
    
    if lista[0][0] in [dicionario_tokens['=='], dicionario_tokens['<>'],
                       dicionario_tokens['<'], dicionario_tokens['<='],
                       dicionario_tokens['>'], dicionario_tokens['>='],
                       dicionario_tokens['=']]:
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
        # Antes de todas as operações (inclusive atribuição e and, or...) verificar se o tipo da esquerda
        # e direita são iguais
        tipos_validos = True
        tipo_esquerda = tipo_valor(esq)
        tipo_direita = tipo_valor(dir)

        if ((tipo_esquerda == 'integer') or (tipo_esquerda == 'real')) and (tipo_direita == 'string'):
            tipos_validos = False
        elif ((tipo_direita == 'integer') or (tipo_direita == 'real')) and (tipo_esquerda == 'string'):
            tipos_validos = False

        if tipos_validos:
            gerador.gera_operacao('+', temp, esq, dir)
            return restoAdd(lista, gerador, temp)
        else:
            raise ErroSemantico(f"Tipos incompatíves para adição: {tipo_esquerda} + {tipo_direita}")
    elif lista[0][0] == dicionario_tokens['-']:
        consome('-', lista)
        dir = mult(lista, gerador)
        temp = gerador.gera_temp()
        # Verificação de tipos para subtração
        tipos_validos = True
        tipo_esquerda = tipo_valor(esq)
        tipo_direita = tipo_valor(dir)
        if ((tipo_esquerda == 'integer') or (tipo_esquerda == 'real')) and (tipo_direita == 'string'):
            tipos_validos = False
        elif ((tipo_direita == 'integer') or (tipo_direita == 'real')) and (tipo_esquerda == 'string'):
            tipos_validos = False
        if tipos_validos:
            gerador.gera_operacao('-', temp, esq, dir)
            return restoAdd(lista, gerador, temp)
        else:
            raise ErroSemantico(f"Tipos incompatíves para subtração: {tipo_esquerda} - {tipo_direita}")
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
        # Verificação de tipos para multiplicação
        tipos_validos = True
        tipo_esquerda = tipo_valor(esq)
        tipo_direita = tipo_valor(dir)
        if ((tipo_esquerda == 'integer') or (tipo_esquerda == 'real')) and (tipo_direita == 'string'):
            tipos_validos = False
        elif ((tipo_direita == 'integer') or (tipo_direita == 'real')) and (tipo_esquerda == 'string'):
            tipos_validos = False
        if tipos_validos:
            gerador.gera_operacao('*', temp, esq, dir)
            return restoMult(lista, gerador, temp)
        else:
            raise ErroSemantico(f"Tipos incompatíves para multiplicação: {tipo_esquerda} * {tipo_direita}")
    elif lista[0][0] == dicionario_tokens['/']:
        consome('/', lista)
        dir = uno(lista, gerador)
        temp = gerador.gera_temp()
        # Verificação de tipos para divisão
        tipos_validos = True
        tipo_esquerda = tipo_valor(esq)
        tipo_direita = tipo_valor(dir)
        if ((tipo_esquerda == 'integer') or (tipo_esquerda == 'real')) and (tipo_direita == 'string'):
            tipos_validos = False
        elif ((tipo_direita == 'integer') or (tipo_direita == 'real')) and (tipo_esquerda == 'string'):
            tipos_validos = False
        if tipos_validos:
            gerador.gera_operacao('/', temp, esq, dir)
            return restoMult(lista, gerador, temp)
        else:
            raise ErroSemantico(f"Tipos incompatíves para divisão: {tipo_esquerda} / {tipo_direita}")
    elif lista[0][0] == dicionario_tokens['mod']:
        consome('mod', lista)
        dir = uno(lista, gerador)
        temp = gerador.gera_temp()
        # Verificação de tipos para mod
        tipos_validos = True
        tipo_esquerda = tipo_valor(esq)
        tipo_direita = tipo_valor(dir)
        if ((tipo_esquerda == 'integer') or (tipo_esquerda == 'real')) and (tipo_direita == 'string'):
            tipos_validos = False
        elif ((tipo_direita == 'integer') or (tipo_direita == 'real')) and (tipo_esquerda == 'string'):
            tipos_validos = False
        if tipos_validos:
            gerador.gera_operacao('mod', temp, esq, dir)
            return restoMult(lista, gerador, temp)
        else:
            raise ErroSemantico(f"Tipos incompatíves para mod: {tipo_esquerda} mod {tipo_direita}")
    elif lista[0][0] == dicionario_tokens['div']:
        consome('div', lista)
        dir = uno(lista, gerador)
        temp = gerador.gera_temp()
        # Verificação de tipos para div
        tipos_validos = True
        tipo_esquerda = tipo_valor(esq)
        tipo_direita = tipo_valor(dir)
        if ((tipo_esquerda == 'integer') or (tipo_esquerda == 'real')) and (tipo_direita == 'string'):
            tipos_validos = False
        elif ((tipo_direita == 'integer') or (tipo_direita == 'real')) and (tipo_esquerda == 'string'):
            tipos_validos = False
        if tipos_validos:
            gerador.gera_operacao('div', temp, esq, dir)
            return restoMult(lista, gerador, temp)
        else:
            raise ErroSemantico(f"Tipos incompatíves para div: {tipo_esquerda} div {tipo_direita}")
    return esq

# Processa operadores unários
def uno(lista, gerador):
    if lista[0][0] == dicionario_tokens['+']:
        consome('+', lista)
        return uno(lista, gerador)
    elif lista[0][0] == dicionario_tokens['-']:
        consome('-', lista)
        return uno(lista, gerador)
    return fator(lista, gerador)

def fator(lista, gerador):
    possibilidades = {'integer', 'float', 'variavel', '(', 'string', 'hexa', 'octal'}
    cod_possibilidades = {dicionario_tokens[i] for i in possibilidades}

    if lista[0][0] in cod_possibilidades:
        if lista[0][0] == dicionario_tokens['integer']:
            valor = int(lista[0][1])
            consome('integer', lista)
            return valor
        elif lista[0][0] == dicionario_tokens['float']:
            valor = float(lista[0][1])
            consome('float', lista)
            return valor
        elif lista[0][0] == dicionario_tokens['hexa']:
            valor = lista[0][1]
            consome('hexa', lista)
            return valor
        elif lista[0][0] == dicionario_tokens['octal']:
            valor = lista[0][1]
            consome('octal', lista)
            return valor
        elif lista[0][0] == dicionario_tokens['variavel']:
            valor = lista[0][1]
            consome('variavel', lista)
            return valor
        elif lista[0][0] == dicionario_tokens['(']:
            consome('(', lista)
            res = expr(lista, gerador)
            consome(')', lista)
            return res
        elif lista[0][0] == dicionario_tokens['string']:
            valor = lista[0][1]
            consome('string', lista)
            return valor
    else:
        print(f"Erro sintático: Esperado 'integer','float', 'variavel', '(' ou 'string' | Recebido: {lista[0][1]} | Linha: {lista[0][2]} | Coluna: {lista[0][3]}")
        exit(1)

#------------------------------
# Sintático
#------------------------------

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

    if len(lista_tokens) == 0:
        print("\nAnálise sintática concluída com sucesso! ✔")
    return gerador.get_codigo()
