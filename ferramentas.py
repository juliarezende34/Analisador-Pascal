from tokenizer import isDelimitador, isOperadorAritmetico, isOperadorComparacao


def digito_hexadecimal(caracter):
    return caracter.isnumeric() or caracter in ['A', 'B', 'C', 'D', 'E', 'F']


# Função que verifica se o pode ser aceito após o hexadecimal
def caracterAceitoAposHexadecimal(caracter):
    return isDelimitador(caracter) or isOperadorAritmetico(caracter) or isOperadorComparacao(caracter)
