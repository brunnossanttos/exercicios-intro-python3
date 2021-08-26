def fatorial(n, show=False):
    """
    -> Calcula fatorial de um numero
    :param n: número a ser calculado
    :param show: opcional, se mostra o calculo ou não
    :return: fatorial de n
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5, show=False))
