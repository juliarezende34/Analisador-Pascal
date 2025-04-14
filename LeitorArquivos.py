from sys import argv
from os import walk


class LeitorArquivos():
    """
    Classe para ler programas em Pascal
    """
    def __init__(self):
        self.ListaNomesDeProgramas = []
        self.ListaProgramasPascal = []
        print(argv)
        
        # Lista de Programas à sererm considerados como entrada
        files = walk(argv[1])
        self.ListaNomesDeProgramas = files.__next__()[2]    # Lendo as entradas
        num_arquivos = len(self.ListaNomesDeProgramas)
        print(f"Lista criada com sucesso, possuindo{num_arquivos} programas!")

    # Lê todos os arquivos de programas em Pascal e os insere em uma lista
    def LerArquivos(self):
        for arquivo in self.ListaNomesDeProgramas:
            try:
                path = argv[1] + "//" + arquivo
                self.ListaProgramasPascal.append(open(f"{path}", 'r'))
            except FileNotFoundError or IOError as e:
                print(f"Problemas na leitura de arquivos \n\n {e} \n\n")
                exit(1)
        print(f" \U0001f389 {len(self.ListaProgramasPascal)} programas lidos!")

    def get_program(self, index):
        """
        Retorna o programa na posição index
        :param index: índice do programa desejado
        :return: programa em Pascal
        """
        return self.ListaProgramasPascal[index].read()
