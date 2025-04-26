
def lendo_float(char_antecessor, char_atual, char_sucessor):
    """
    Verifica se um float em pascal está sendo lido pelo interpretador com base no último, próximo e atual caracteres lidos.
    :param char_antecessor: Último caracter à ser lido.
    :param char_atual: Caractere atual.
    :param char_sucessor: Próximo caracter à ser lido.
    :return: True se for um ponto flutuante, False caso contrário.
    """
    vizinhos_numericos = char_antecessor.isnumeric() and char_sucessor.isnumeric()
    if char_atual == '.' and vizinhos_numericos:
        return True
    else:
        return False