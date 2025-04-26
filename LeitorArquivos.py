from sys import argv
from os import walk


class LeitorArquivos():
    """
    Classe para ler programas em Pascal
    """
    def __init__(self):
        self.ListaNomesDeProgramas = []
        self.ListaProgramasPascal = []
        self.DicionarioProgramasPascal = {}
        self.path = argv[1] + "/"

        # Lista de Programas à sererm considerados como entrada
        files = walk(argv[1])
        self.ListaNomesDeProgramas = files.__next__()[2]    # Lendo as entradas
        num_arquivos = len(self.ListaNomesDeProgramas)
        print(f"Lista criada com sucesso, possuindo {num_arquivos} programas!")

    # # Lê todos os arquivos de programas em Pascal e os insere em uma lista
    # def LerArquivos(self):
    #     for arquivo in self.ListaNomesDeProgramas:
    #         try:
    #             self.ListaProgramasPascal.append(open(f"{self.path+arquivo}", 'r', encoding='utf-8'))
    #         except UnicodeDecodeError:
    #             print(f"Problemas na leitura de arquivos \n\n {arquivo} com latin 1...\n\n")
    #             self.ListaProgramasPascal.append(open(f"{self.path+arquivo}", 'r', encoding='latin 1'))
    #         except FileNotFoundError or IOError as e:
    #             print(f"Problemas na leitura de arquivos \n\n {e} \n\n")
    #             exit(1)
    #     print(f" \U0001f389 {len(self.ListaProgramasPascal)} programas lidos!")

    #     for i, j in zip(self.ListaNomesDeProgramas, self.ListaProgramasPascal):
    #         self.DicionarioProgramasPascal[i] = j

    def LerArquivos(self):
    
        NomesDeProgramasOrdenados = sorted(self.ListaNomesDeProgramas, key=self.ordenar_nomes_de_arquivos)
        for arquivo in NomesDeProgramasOrdenados:
            caminho_completo = f"{self.path}{arquivo}"
            try:
                # Tenta ler com UTF-8 primeiro
                with open(caminho_completo, 'r', encoding='utf-8') as f:
                    conteudo = f.read()
            except UnicodeDecodeError:
                # Se falhar, tenta Latin-1 (com fallback para outros encodings)
                try:
                    with open(caminho_completo, 'r', encoding='latin-1') as f:
                        conteudo = f.read()
                except Exception as e:
                    print(f"Falha ao ler {arquivo}: {str(e)}")
                    exit(1)
            except (FileNotFoundError, IOError) as e:
                print(f"Erro de arquivo: {str(e)}")
                exit(1)
            
            # Armazena o conteúdo JÁ LIDO (não o arquivo aberto)
            self.ListaProgramasPascal.append(conteudo)
            self.DicionarioProgramasPascal[arquivo] = conteudo.split('\n')

        print(f" \U0001f389 {len(self.ListaProgramasPascal)} programas lidos!")

    def get_program_index(self, index):
        """
        Retorna o programa na posição index
        :param index: índice do programa desejado
        :return: programa em Pascal
        """
        return self.ListaProgramasPascal[index].read()

    def get_program_name(self, name):
        """
        Retorna o programa de nome específico no diretório inputs
        :param name: nome do programa desejado
        :return: nome do programa em Pascal
        """
        return self.DicionarioProgramasPascal[f"{name}"].read()

    def get_lines_program(self, name):
        """
        Retorna as linhas do programa de nome específico no diretório inputs
        :param name: nome do programa desejado
        :return: linhas do programa em Pascal
        """
        return self.DicionarioProgramasPascal[f"{name}"].read().split('\n')

    

    def ordenar_nomes_de_arquivos(self, nome_do_arquivo):
        """
        Ordena a lista de nomes de arquivos
        """
        numero_str = ""
        for char in nome_do_arquivo:
            if char.isdigit():
                numero_str += char
    
        return int(numero_str) if numero_str else 0
    

        