from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou impar?[P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}, o resultado da soma é {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU!!!')
            v += 1
        else:
            print('VOCÊ PERDEU!!!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCÊ VENCEU!!!')
            v += 1
        else:
            print('VOCÊ PERDEU!!!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER\nVocê venceu {v} partida(s) seguida(s)')
