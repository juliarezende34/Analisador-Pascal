def lendo_float(char_antecessor, char_atual, char_sucessor):
    """
    Verifica se um float em pascal está sendo lido pelo interpretador.
    :param char_antecessor: Último caracter à ser lido.
    :param char_atual: Caractere atual.
    :param char_sucessor: Próximo caracter à ser lido.
    :return: True se for um ponto flutuante, False caso contrário.
    """
    antecessor_numerico = char_antecessor.isnumeric()
    sucessor_numerico = char_sucessor.isnumeric()

    vizinhos_numericos = antecessor_numerico and sucessor_numerico
    if char_atual == '.' and vizinhos_numericos:
        return True
    else:
        return False


def is_hex(palavra):
    """
    Verifica se o número é hexadecimal.
    :return: True se for hexadecimal, False caso contrário.
    :param palavra: Palavra a ser verificada.
    """
    if len(palavra) < 3:
        return False
    else:
        if palavra[0] == '0' and palavra[1] == 'x':
            return True

        else:
            return False


def is_float(palavra):
    """
    Verifica se a palavra lida é um float escrito em Pascal
    :return: True se for float, False caso contrário.
    :param palavra: Palavra a ser verificada.
    """
    inteiros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    ponto = False
    for i, v in enumerate(palavra):
        if ponto == False and palavra[i] == '.':
            ponto = True
            continue
        else:
            if v not in inteiros:
                if ponto == True and palavra[i] == '.':
                    print("Erro léxico: caractere inválido: ", palavra)
                    exit(1)
                else:
                    return False

    return True


def is_octal(palavra):
    """
    Verifica se a palavra é um octal escrito em Pascal
    :return: True se for octal, False caso contrário.
    :param palavra: Palavra a ser verificada.
    """
    inteiros = ['0', '1', '2', '3', '4', '5', '6', '7']
    if palavra[0] == '0':
        for i in palavra:
            if i not in inteiros:
                return False
        return True

    else:
        return False


def is_int(palavra):
    """
    Verifica se a palavra lida é um inteiro escrito em Pascal
    :return: True se for inteiro, False caso contrário.
    :param palavra: Palavra a ser verificada.
    """
    inteiros = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    if palavra[0] == '0':
        return False
    else:
        for i in palavra:
            if i not in inteiros:
                return False
        return True