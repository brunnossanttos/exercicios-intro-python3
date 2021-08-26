cont = 0
while True:
    print('=-='*10)
    n = int(input('Qual número você deseja calcular a tabuada? '))

    if n > 0:
        for cont in range(0, 11):
            soma = n * cont
            print(f'{cont} x {n} = {soma}')
            cont += 1
    else:
        break
