from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-'* 20)
print('VOU PENSAR EM UM NÚMERO de 0 a 5....')
print('-=-'* 20)
nsorte = int(input('Em qual número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if nsorte == computador:
    print('Você acertou, eu pensei no número {}'.format(computador))
else:
    print('Você perdeu... Era o número {} , não o número {}'.format(computador, nsorte))
