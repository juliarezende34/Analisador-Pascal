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

    # Lê todos os arquivos de programas em Pascal e os insere em uma lista
    def LerArquivos(self):
        for arquivo in self.ListaNomesDeProgramas:
            try:
                self.ListaProgramasPascal.append(
                    open(f"{self.path+arquivo}", 'r', encoding='utf-8')
                )

            except FileNotFoundError or IOError as e:
                print(f"Problemas na leitura de arquivos \n\n {e} \n\n")
                exit(1)
        print(f" \U0001f389 {len(self.ListaProgramasPascal)} programas lidos!")

        for i, j in zip(self.ListaNomesDeProgramas, self.ListaProgramasPascal):
            self.DicionarioProgramasPascal[i] = j

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