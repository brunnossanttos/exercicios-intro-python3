from random import randint
numeros = list()


def sorteia():
    """
    -> sorteia cinco números de 0 a 9.
    :return: números sorteados
    """
    for c in range(0, 5):
        numeros.append(randint(0, 9))
    print(f'Os valores sorteados foram {numeros}.')


def somapar(lista):
    """

    :param lista: lista de números sorteados
    :return: soma dos números pares
    """
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares temos {soma}')


sorteia()
somapar(numeros)
