num = int(input('Digite o número que deseja vê a tabuada: '))
print('=-='*15)
print('      TABUADA de {}'.format(num))
print('=-='*15)
for c in range(0, 11):
    soma = num * c
    print('{} x {} = {}'.format(c, num, soma))
print('=-='*15)
