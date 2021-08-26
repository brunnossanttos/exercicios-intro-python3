listanum = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}o valor: '))
    if valor % 2 == 0:
        listanum[0].append(valor)
    elif valor % 2 == 1:
        listanum[1].append(valor)
print('=-' * 25)
listanum[0].sort()
listanum[1].sort()
print(f'Os números pares digitados foram {listanum[0]}')
print(f'Os números impares digitados foram {listanum[1]}')
print('=-' * 25)
