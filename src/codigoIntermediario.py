# codigoIntermediario.py
from tokenizer import mapeamento_operadores

# Classe responsável por gerar o código intermediário
class GeradorCodigoIntermediario:
    def __init__(self):
        # Lista que armazena todas as tuplas do código intermediário
        self.codigo = []
        # Contadores para criação de temporários e labels únicos
        self.contador_temp = 0
        self.contador_label = 0
        # Tabela de símbolos que armazena tipo de variáveis declaradas
        self.tabela_simbolos = {}
        # Pilhas de controle para break e continue (em laços)
        self.pilha_labels = []
        self.pilha_break = []
        self.pilha_continue = []

    # Gera uma variável temporária única (ex: _t1, _t2, ...)
    def gera_temp(self):
        self.contador_temp += 1
        return f"_t{self.contador_temp}"

    # Gera um label único (ex: LABEL1, FOR_START2, etc.)
    def gera_label(self, prefixo="LABEL"):
        self.contador_label += 1
        return f"{prefixo}{self.contador_label}"

    # Gera instrução de declaração de variável com valor inicial
    def gera_declaracao(self, nome, tipo):
        if nome in self.tabela_simbolos:
            return  # Ignora se já foi declarado

        # Define valor padrão baseado no tipo
        valor_inicial = (
            '0' if tipo == "integer" 
            else '0.0' if tipo == "real" 
            else "" if tipo == "string" 
            else None
        )

        # Adiciona instrução e salva na tabela de símbolos
        if valor_inicial is not None:
            self.tabela_simbolos[nome] = tipo
            self.codigo.append(("ATT", nome, valor_inicial, tipo))

    # Gera instrução de atribuição (destino := valor)
    def gera_atribuicao(self, destino, valor):

        # Verifica se é possível fundir com operação anterior
        if isinstance(valor, str) and valor.startswith("_t") and len(self.codigo) > 0:
            ultima_instr = self.codigo[-1]
            op_aritmeticos = {"ADD", "SUB", "MULT", "FDIV", "DIV", "MOD"}

            if (
                ultima_instr[0] in op_aritmeticos
                and ultima_instr[1] == valor  # temp gerado
                and ultima_instr[2] == destino  # op1 é a variável destino
            ):
                # Substitui operação por uma versão direta
                self.codigo[-1] = (ultima_instr[0], destino, destino, ultima_instr[3])
                return

        # Inferência de tipo para variáveis ainda não declaradas
        if destino not in self.tabela_simbolos:
            tipo = (
                "integer" if isinstance(valor, int) or (isinstance(valor, str) and valor.isdigit())
                else "real" if isinstance(valor, float)
                else "string"
            )
            self.tabela_simbolos[destino] = tipo
        else:
            tipo = self.tabela_simbolos[destino]

        self.codigo.append(("ATT", destino, valor, tipo))

    # Gera operação intermediária (ex: ADD, SUB, EQ, etc.)
    def gera_operacao(self, operador, destino, op1, op2=None):
        op_code = mapeamento_operadores[operador]

        if op2 is None:
            self.codigo.append((op_code, destino, op1))
        else:
            self.codigo.append((op_code, destino, op1, op2))

        return destino  # Retorna o temporário gerado

    # Gera uma condição com salto condicional (IF)
    def gerar_condicao(self, condicao, label_true, label_false):
        # Gera labels automaticamente se não forem fornecidos
        if label_true is None:
            label_true = self.gera_label("IF_TRUE")
        if label_false is None:
            label_false = self.gera_label("ELSE")

        # Instrução IF que redireciona para um dos dois caminhos
        self.codigo.append(("IF", condicao, label_true, label_false))
        # Gera label do bloco verdadeiro
        self.codigo.append(("LABEL", label_true, None, None))
        return label_true, label_false

    # Gera um salto incondicional
    def gerar_jump(self, label):
        self.codigo.append(("JUMP", label, None, None))

    # Gera um label manual
    def gerar_label(self, label):
        self.codigo.append(("LABEL", label, None, None))

    # Gera o código completo de um laço for
    # def gerar_for(self, var, inicio, fim, corpo_callback):
    #     # Geração de labels únicos para controle do laço
    #     label_start = self.gera_label("FOR_START")
    #     label_body = self.gera_label("FOR_BODY")
    #     label_continue = self.gera_label("FOR_CONTINUE")
    #     label_end = self.gera_label("FOR_END")

    #     # Inicializa variável de controle do for
    #     self.gera_atribuicao(var, inicio)

    #     # Label do início do for
    #     self.gerar_label(label_start)

    #     # Gera condição de parada (var <= fim)
    #     temp_cond = self.gera_temp()
    #     self.gera_operacao("<=", temp_cond, var, fim)

    #     # Salta para corpo ou fim do laço
    #     self.codigo.append(("IF", temp_cond, label_body, label_end))

    #     # Label do corpo do laço
    #     self.gerar_label(label_body)

    #     # Controla contexto para uso de break e continue
    #     self.pilha_break.append(label_end)
    #     self.pilha_continue.append(label_continue)

    #     # Executa corpo do for via callback
    #     corpo_callback(label_continue, label_end)

    #     # Label de continue (incrementa e volta)
    #     self.gerar_label(label_continue)
    #     temp_inc = self.gera_temp()
    #     self.gera_operacao("+", temp_inc, var, 1)  # Corrigido: incremento numérico
    #     self.gera_atribuicao(var, temp_inc)

    #     # Volta ao início do for
    #     self.gerar_jump(label_start)

    #     # Label de fim do laço
    #     self.gerar_label(label_end)

    #     # Sai do contexto de break/continue
    #     self.pilha_break.pop()
    #     self.pilha_continue.pop()

    def gerar_for(self, var, inicio, fim, corpo_callback):
        label_start = self.gera_label("FOR_START")
        label_body = self.gera_label("FOR_BODY")
        label_end = self.gera_label("FOR_END")

        # Inicializa variável de controle do for
        self.gera_atribuicao(var, inicio)  # ex: ('ATT', 'i', 1.0, 'real')

        # Decremento antes do loop
        self.gera_operacao("-", var, var, 1)  # ex: ('SUB', 'i', 'i', 1.0)

        # Label de início do for
        self.gerar_label(label_start)

        # Incrementa antes de testar
        self.gera_operacao("+", var, var, 1)  # ex: ('ADD', 'i', 'i', 1.0)

        # Condição de parada
        temp_cond = self.gera_temp()
        self.gera_operacao("<=", temp_cond, var, fim)

        # Se for verdadeiro, entra no corpo; senão, vai pro fim
        self.codigo.append(("IF", temp_cond, label_body, label_end))

        # Corpo do laço
        self.gerar_label(label_body)

        # Push dos labels (break só precisa saber onde terminar)
        self.pilha_break.append(label_end)
        self.pilha_continue.append(label_start)  # agora continue volta direto pro início

        # Executa corpo do laço
        corpo_callback(label_start, label_end)

        # Volta pro início do for
        self.gerar_jump(label_start)

        # Label de fim
        self.gerar_label(label_end)

        # Sai do contexto de break/continue
        self.pilha_break.pop()
        self.pilha_continue.pop()

    # Gera leitura de entrada (ex: read(x))
    def gera_leitura(self, variavel, tipo):
        self.codigo.append(("CALL", "SCAN", variavel, tipo))

    # Gera escrita de saída (ex: write(x))
    def gera_escrita(self, valor):
        # Se for uma variável conhecida, pega o tipo da tabela
        if valor in self.tabela_simbolos:
            tipo = self.tabela_simbolos[valor]
        else:
            # Se for literal, tenta inferir o tipo
            if isinstance(valor, str):
                if valor.startswith("'") and valor.endswith("'"):
                    tipo = "string"
                elif valor.replace('.', '', 1).isdigit():
                    tipo = "real" if '.' in valor else "integer"
                else:
                    tipo = "string"  # assume string genérica para casos como 'Resultado: '
            elif isinstance(valor, int):
                tipo = "integer"
            elif isinstance(valor, float):
                tipo = "real"
            else:
                tipo = None

        self.codigo.append(("CALL", "PRINT", valor, tipo))


    # Retorna a lista de tuplas geradas
    def get_codigo(self):
        return self.codigo

    # Reseta o gerador (útil para múltiplas execuções)
    def limpar_codigo(self):
        self.codigo = []
        self.contador_temp = 0
        self.contador_label = 0
        self.tabela_simbolos = {}

# Exceção customizada para erros semânticos
class ErroSemantico(Exception):
    pass
