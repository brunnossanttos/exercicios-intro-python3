from random import randint
from time import sleep
lista = list()
jogos = list()
print('-=' * 15)
print('          MEGA-SENA       ')
print('-=' * 15)
quant = int(input('Quantos jogos você quer? '))
totjogos = 1
while totjogos <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    totjogos += 1
print('=-' * 3, f'Sorteando', '=-' * 3)
sleep(2)
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1} : {l}')
    sleep(1)
print('=-' * 3, 'BOA SORTE', '=-' * 3)
