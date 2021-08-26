def mostralin():
    """

    :return: mostra linha
    autor Bruno Santos
    """
    print('*--*' * 15)


def voto(ano):
    """

    :param ano: Recebe ano de nascimento
    :return: idade, se voto é obrigatótio ou não.
    """
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    mostralin()
    print(f'A idade é: {idade} anos')
    if idade >= 65:
        return f'Com {idade} anos: Voto Opcional'
    elif 18 <= idade <= 64:
        return f'Com {idade} anos: Voto obrigatório!!!'
    elif 16 <= idade <= 17:
        return f'Com {idade} anos: Voto não é obrigatório.'
    elif idade <= 15:
        f'Com {idade} anos: Não vota.'


# Programa Principal
help(voto)
while True:
    mostralin()
    anonasc = int(input('Em que ano você nasceu? '))
    print(voto(anonasc))
    while True:
        mostralin()
        resp = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        else:
            print('ERRO!!! Use apenas S ou N')
    if resp == 'N':
        break
    print()
mostralin()
print('FIM')
