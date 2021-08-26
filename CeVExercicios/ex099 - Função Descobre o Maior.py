from random import randint
from time import sleep


def maior(numeros):
    print('-=' * 30)
    mvalor = max(numeros)
    print('\nAnalisando os valores passados... ')
    for n in numeros:
        print(f'{n} ', end=' ')
        sleep(0.5)
    print(f'\nForam informados(s) {len(numeros)} valores ao todo.')
    print()
    print(f'O maior valor informado foi {mvalor}')
    sleep(1)


valores = list()
numero = list()
for i in range(1, 5):
    tm = randint(1, 10)
    numero.clear()
    for j in range(0, tm):
        numero.append(randint(0, 50))
    valores.append(numero[:])
for i in range(0, len(valores)):
    maior(valores[i])
