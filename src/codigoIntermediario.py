from tokenizer import mapeamento_operadores

class GeradorCodigoIntermediario:
    def __init__(self):
        self.codigo = []  # Lista de tuplas do código intermediário
        self.contador_temp = 0  # Contador para variáveis temporárias
        self.contador_label = 0  # Contador para labels
        self.tabela_simbolos = {}  # Para análise semântica
        self.pilha_labels = []  # Para controle de fluxo aninhado


    # ---------------- GERADORES DE NOMES AUXILIARES ----------------

    # Gera nome de variável temporária (ex: _t1, _t2)
    def gera_temp(self):
        self.contador_temp += 1
        return f"_t{self.contador_temp}"

    # Gera nome de label (ex: LABEL1, LOOP2)
    def gera_label(self, prefixo="LABEL"):
        self.contador_label += 1
        return f"{prefixo}{self.contador_label}"
    

    # ---------------- DECLARAÇÕES E ATRIBUIÇÕES ----------------

    # Gera código para declaração de variável com valor padrão
    def gera_declaracao(self, nome, tipo):
        valor_inicial = (
            0 if tipo == "integer" 
            else 0.0 if tipo == "real" 
            else "" if tipo == "string" 
            else None
        )
        if valor_inicial is not None:
            self.codigo.append(("=", nome, valor_inicial, None))
            self.tabela_simbolos[nome] = tipo

    # Gera código para atribuição simples
    def gera_atribuicao(self, destino, valor):
        self.codigo.append(("=", destino, valor, None))
        if destino not in self.tabela_simbolos:
            tipo = (
                "integer" if isinstance(valor, int)
                else "real" if isinstance(valor, float)
                else "string"
            )
            self.tabela_simbolos[destino] = tipo


    # ---------------- OPERAÇÕES ARITMÉTICAS E LÓGICAS ----------------

    # Gera código para operação convertendo operadores
    def gera_operacao(self, operador, destino, op1, op2=None):
        
        op_code = mapeamento_operadores[operador]
        
        if op2 is None:  # Operação unária
            self.codigo.append((op_code, destino, op1))
        else:  # Operação binária
            self.codigo.append((op_code, destino, op1, op2))
        return destino

    # Verifica se operando é válido (semântica)
    def _verificar_operando(self, operando):
        if isinstance(operando, str) and operando not in self.tabela_simbolos and not operando.startswith("_t"):
            raise ErroSemantico(f"Operando '{operando}' não declarado")
        

    # ---------------- CONTROLE DE FLUXO ----------------

    # Gera label para início de loop (FOR/WHILE)
    def iniciar_loop(self):
        label_inicio = self.gera_label("LOOP")
        self.codigo.append(("LABEL", label_inicio, None, None))
        self.pilha_labels.append(label_inicio)
        return label_inicio

    # Gera código para condicional (IF/WHILE)
    def gerar_condicao(self, condicao, label_true, label_false):
        self.codigo.append(("IF", condicao, label_true, label_false))

    # Gera instrução de salto incondicional
    def gerar_jump(self, label):  
        self.codigo.append(("JUMP", label, None, None))

    # Finaliza estrutura de loop
    def finalizar_loop(self, label_fim):
        self.gerar_jump(self.pilha_labels.pop())
        self.codigo.append(("LABEL", label_fim, None, None))


    # ---------------- ENTRADA/SAÍDA ----------------
    
    # Gera código para leitura de entrada
    def gera_leitura(self, variavel, tipo):
        self.codigo.append(("CALL", "READ", variavel, tipo))

    # Gera código para escrita de saída
    def gera_escrita(self, valor):
        
        if isinstance(valor, str) and valor.startswith("'") and valor.endswith("'"):
            # Se for string literal (incluindo '\n')
            self.codigo.append(("CALL", "PRINT", valor, None))
        else:
            # Se for variável ou valor numérico
            self.codigo.append(("CALL", "PRINT", valor, None))


    # ---------------- UTILIDADES ----------------

    # Retorna o código intermediário gerado
    def get_codigo(self):
        return self.codigo

    # Reseta o gerador para novo uso
    def limpar_codigo(self):
        self.codigo = []
        self.contador_temp = 0
        self.contador_label = 0
        self.tabela_simbolos = {}


class ErroSemantico(Exception):
    # Exceção para erros semânticos
    pass