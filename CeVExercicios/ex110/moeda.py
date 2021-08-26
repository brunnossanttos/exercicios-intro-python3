def aumentar(preco=0, taxa=0, formato=False):
    '''

    :param preco: Recebe um valor float
    :param taxa: Recebe um valor inteiro
    :param formato: Recebe um valor lógico
    :return: preço mais a taxa em porcetagem
    '''
    res = preco + (preco * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if formato is False else moeda(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if formato is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>2.2f}'.replace('.', ',')


def resumo(preco=0, taxa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco,True)}')
    print(f'{taxa}% de aumento: \t{aumentar(preco, taxa, True)}')
    print(f'{taxar}% de redução: \t\t{diminuir(preco, taxar, True)}')
    print('-' * 30)
