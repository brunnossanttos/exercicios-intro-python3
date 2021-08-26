from random import randint
from time import sleep
print('-=-'*10)
print('          JuKenPô')
print('-=-'*10)
jogador = int(input('Escolha:\n0 = Pedra. 1 = Papel. 2 = Tesoura: '))
computador = randint(0, 2)
if computador == 0 and jogador == 1:
    print('Coloquei pedra, e você papel...')
    sleep(2)
    print('Você venceu... T_T')
elif computador == 0 and jogador == 2:
    print('Eu coloquei pedra, e Você tesoura...')
    sleep(2)
    print('Você perdeu, HAHAHA!!!')
elif computador == 1 and jogador == 0:
    print('Eu coloquei papel, e você pedra...')
    sleep(2)
    print('Você perdeu, HAHAHA!!!')
elif computador == 1 and jogador == 2:
    print('Eu coloquei papel, e você tesoura...')
    sleep(2)
    print('Você venceu... T_T')
elif computador == 2 and jogador == 0:
    print('Eu coloquei tesoura, e você pedra...')
    sleep(2)
    print('Você venceu... T_T')
elif computador == 2 and jogador == 1:
    print('Coloquei Tesoura, e você papel...')
    sleep(2)
    print('Você perdeu... HAHAHA!!!')
else:
    print('EMPATE... VAMOS JOGAR NOVAMENTE')
