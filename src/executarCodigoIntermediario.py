def output_intermediario(lista):
    """
    Escreve o código intermediário gerado pelo analisador sintático em um arquivo de texto.
    """
    if not lista:
        print("Nenhum código intermediário para colocar no arquivo.")
        return
    
    with open('../output/codigo_intermediario.txt', 'w', encoding='utf-8') as f:
        for comando in lista:
            f.write(f"{comando}\n")
        f.close()

def processar_labels(lista):
    """
    Processa as labels no código intermediário e retorna um dicionário com os rótulos e seus respectivos índices.
    """
    dict_labels = {}
    for i, comando in enumerate(lista):
        if comando[0] == 'LABEL':
            label_name = comando[1]
            if label_name not in dict_labels:
                dict_labels[label_name] = i
            else:
                print(f"Aviso: A label '{label_name}' já foi definida anteriormente. Linha {i + 1}.")
    return dict_labels

def get_valor_literal_ou_variavel(valor, dict_variaveis, i):
    """
    Tenta retornar o valor de uma variável ou literal passado como string.
    """
    try:
        return int(valor)
    except ValueError:
        pass

    try:
        return float(valor)
    except ValueError:
        pass

    if valor in dict_variaveis:
        return dict_variaveis[valor]
    else:
        print(f"Erro: A variável '{valor}' não foi definida antes de ser usada. Linha {i}.")
        exit(1)


            
def chamada_sistema(tupla, dict_variaveis, i):
    if tupla[1] == 'PRINT':
        if tupla[2] in dict_variaveis.keys():
            imprimir = dict_variaveis[tupla[2]]
        else:
            imprimir = tupla[2]
        print(imprimir)

    elif tupla[1] == 'SCAN':
        variavel_scan = tupla[2]
        if variavel_scan not in dict_variaveis:
            print(f"Erro: Variável '{variavel_scan}' não foi declarada antes da leitura. Linha {i + 1}.")
            exit(1)
        valor_scan = input(f"Digite o valor para a variável '{variavel_scan}': ")
        try:
            valor_scan = int(valor_scan)
        except ValueError:
            try:
                valor_scan = float(valor_scan)
            except ValueError:
                pass  # Mantém como string
        
        tipo_valido = False
        if tupla[3] == 'integer':
            if type(valor_scan) == type(2):
                tipo_valido = True
        elif tupla[3] == 'string':
            if type(valor_scan) == type('text'):
                tipo_valido = True
        elif tupla[3] == 'real':
            if type(valor_scan) == type(3.5):
                tipo_valido = True
        
        if tipo_valido:
            dict_variaveis[variavel_scan] = valor_scan
        else:
            print(f"Erro durante o SCAN. Tipo esperado: {tupla[3]} | Tipo recebido: {type(valor_scan)} ")
            exit(1)

    else:
        print(f"Aviso: Chamada de sistema '{tupla[1]}' não reconhecida. Linha {i + 1}.")
        exit(1)

def executar_operacoes_aritmeticas(tupla, dict_variaveis, i):
    """
    Executa operações aritméticas e retorna o resultado.
    """
    operador = tupla[0]
    destino = tupla[1]
    op1 = tupla[2]
    op2 = tupla[3]

    if (destino in dict_variaveis.keys()) or destino.startswith('_t'):
        # op1 pode ser: op1 = '1' ou op1 = 'variavel'
        if op1 in dict_variaveis.keys():
            valor_op1 = dict_variaveis[op1]
        else:
            valor_op1 = get_valor_literal_ou_variavel(op1, dict_variaveis,i)
        
        # op2 pode ser: op2 = '1' ou op2 = 'variavel'
        if op2 in dict_variaveis.keys():
            valor_op2 = dict_variaveis[op2]
        else:
            valor_op2 = get_valor_literal_ou_variavel(op2, dict_variaveis,i)

        if operador == 'ADD':
            dict_variaveis[destino] = valor_op1 + (valor_op2)
        elif operador == 'SUB':
            dict_variaveis[destino] = valor_op1 - (valor_op2)
        elif operador == 'MULT':
            dict_variaveis[destino] = valor_op1 * (valor_op2)
        elif operador == 'FDIV':
            if valor_op2 == 0:
                print(f"Erro: Divisão por zero. Linha {i + 1}.")
                exit(1)
            dict_variaveis[destino] = valor_op1 / (valor_op2)
        elif operador == 'IDIV':
            if valor_op2 == 0:
                print(f"Erro: Divisão por zero. Linha {i + 1}.")
                exit(1)
            dict_variaveis[destino] = int(valor_op1 // (valor_op2))
        elif operador == 'MOD':
            if valor_op2 == 0:
                print(f"Erro: Divisão por zero. Linha {i + 1}.")
                exit(1)
            dict_variaveis[destino] = valor_op1 % (valor_op2)
        else:
            print(f"Erro: Operador '{operador}' não reconhecido. Linha {i + 1}.")
            exit(1)
    else:
        print(f"Erro: Variável '{destino}' não foi declarada antes da operação. Linha {i + 1}.")
        exit(1)
    
def executar_operacoes_relacionais(tupla, dict_variaveis, i):
    """
    Executa operações relacionais e retorna o resultado.
    """
    operador = tupla[0]
    destino = tupla[1]
    op1 = tupla[2]
    op2 = tupla[3]

    if (destino in dict_variaveis) or destino.startswith('_t'):
        # op1 pode ser: op1 = '1' ou op1 = 'variavel'
        if op1 in dict_variaveis.keys():
            valor_op1 = dict_variaveis[op1]
        else:
            valor_op1 = get_valor_literal_ou_variavel(op1, dict_variaveis,i)
        
        # op2 pode ser: op2 = '1' ou op2 = 'variavel'
        if op2 in dict_variaveis.keys():
            valor_op2 = dict_variaveis[op2]
        else:
            valor_op2 = get_valor_literal_ou_variavel(op2, dict_variaveis,i)
        ############################################################################################ Exceto o == e !=, o tipo dos operadores deve ser de número
        if operador == 'LEQ':
            dict_variaveis[destino] = (valor_op1 <= valor_op2)
        elif operador == 'LESS':
            dict_variaveis[destino] = (valor_op1 < valor_op2)
        elif operador == 'GEQ':
            dict_variaveis[destino] = (valor_op1 >= valor_op2)
        elif operador == 'GRET':
            dict_variaveis[destino] = (valor_op1 > valor_op2)
        elif operador == 'EQ':
            dict_variaveis[destino] = (valor_op1 == valor_op2)
        elif operador == 'NEQ':
            dict_variaveis[destino] = (valor_op1 != valor_op2)
        else:
            print(f"Erro: Operador relacional '{operador}' não reconhecido. Linha {i + 1}.")
            exit(1)
   
    else:
        print(f"Erro: Variável '{destino}' não foi declarada antes da operação. Linha {i + 1}.")
        exit(1)

def executar_operacoes_logicas(tupla, dict_variaveis, i):
    """
    Executa operações lógicas e retorna o resultado.
    """
    operador = tupla[0]
    destino = tupla[1]
    op1 = tupla[2]
    op2 = tupla[3] 

    if (destino in dict_variaveis) or destino.startswith('_t'):
        # op1 pode ser: op1 = '1' ou op1 = 'variavel'
        if op1 in dict_variaveis.keys():
            valor_op1 = dict_variaveis[op1]
        else:
            valor_op1 = get_valor_literal_ou_variavel(op1, dict_variaveis,i)
        
        # op2 pode ser: op2 = '1' ou op2 = 'variavel'
        if op2 in dict_variaveis.keys():
            valor_op2 = dict_variaveis[op2]
        else:
            valor_op2 = get_valor_literal_ou_variavel(op2, dict_variaveis,i)

        if operador == 'AND':
            dict_variaveis[destino] = (valor_op1 and valor_op2)
        elif operador == 'OR':
            dict_variaveis[destino] = (valor_op1 or valor_op2)
        elif operador == 'NOT':
            dict_variaveis[destino] = (not valor_op1)
        else:
            print(f"Erro: Operador lógico '{operador}' não reconhecido. Linha {i + 1}.")
            exit(1)
    
    else:
        print(f"Erro: Variável '{destino}' não foi declarada antes da operação. Linha {i + 1}.")
        exit(1)

def processar_condicional(tupla, dict_variaveis, dict_labels, i):
    """
    Processa uma condição e executa o salto condicional.
    """
    op = tupla[1]
    label_true = tupla[2]
    label_false = tupla[3]

    if op in dict_variaveis.keys():
        if dict_variaveis[op]:
            return dict_labels[label_true]
        else:
            return dict_labels[label_false]
    else:
        print(f"Erro: Variável '{op}' não foi declarada antes da operação condicional. Linha {i + 1}.")
        exit(1)

def executar_intermediario(lista):
    """
    Executa o código intermediário gerado pelo analisador sintático.
    """
    if not lista:
        print("Nenhum código intermediário para executar.")
        return

    dict_labels = processar_labels(lista)
    dict_variaveis = {}
    operacoes_aritmeticas = {'ADD', 'SUB', 'MULT', 'FDIV', 'IDIV', 'MOD'}
    operacoes_relacionais = {'LEQ', 'LESS', 'GEQ', 'GRET', 'EQ', 'NEQ'}
    operacoes_logicas = {'AND', 'OR', 'NOT'}

    program_counter = 0

    while program_counter < len(lista):
        tupla_atual = lista[program_counter]
        # Atribuição
        if tupla_atual[0] == 'ATT':
            variavel = tupla_atual[1]
            if tupla_atual[2] != '':
                valor = get_valor_literal_ou_variavel(tupla_atual[2], dict_variaveis, program_counter + 1)
            else:
                valor = ''
            dict_variaveis[variavel] = valor

        # Chamada de sistema
        elif tupla_atual[0] == 'CALL':
            chamada_sistema(tupla_atual, dict_variaveis, program_counter + 1)
        
        # Operações aritméticas
        elif tupla_atual[0] in operacoes_aritmeticas:
            executar_operacoes_aritmeticas(tupla_atual, dict_variaveis, program_counter + 1)
        
        # Operações relacionais
        elif tupla_atual[0] in operacoes_relacionais:
            executar_operacoes_relacionais(tupla_atual, dict_variaveis, program_counter + 1)
        
        # Operações lógicas
        elif tupla_atual[0] in operacoes_logicas:
            executar_operacoes_logicas(tupla_atual, dict_variaveis, program_counter + 1)
        
        # Jump
        elif tupla_atual[0] == 'JUMP':
            label = tupla_atual[1]
            if label in dict_labels:
                program_counter = dict_labels[label]
                continue
            else:
                print(f"Erro: Label '{label}' não encontrada. Linha {program_counter + 1}.")
                exit(1)

        # Condicional
        elif tupla_atual[0] == 'IF':
            program_counter = processar_condicional(tupla_atual, dict_variaveis, dict_labels,program_counter + 1)
            continue

        if (tupla_atual[0] != 'JUMP') and (tupla_atual[0] != 'IF'):
            # Incrementa o contador de programa apenas se não for um salto
            program_counter += 1

    # Escreve o resultado das variáveis no arquivo de saída
    with open('../output/resultado_execucao_intermediario.txt', 'w', encoding='utf-8') as f:
        for variavel, valor in dict_variaveis.items():
            f.write(f"{variavel} = {valor}\n")