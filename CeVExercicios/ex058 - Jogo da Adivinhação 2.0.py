from random import randint
computador = randint(0, 10)
cont = 0
print('-=-'*20)
print('Olá, sou seu computador.\nVou pensar em número de 0 a 10...')
print('-=-'*20)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente Novamente.')
        else:
            print('Menos... Tente novamente.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
