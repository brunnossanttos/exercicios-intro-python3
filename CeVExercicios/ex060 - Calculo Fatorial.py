n = int(input('Digite um número para calcular o fatorial: '))
c = n
f = 1
print(f'Calculando {n}!...')
while c > 0:
    print('{} '.format(c), end='')
    print('x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')