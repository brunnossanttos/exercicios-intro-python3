print('==='*15)
print('|    10 TERMOS DE PROGRESSÃO ARITMÉTICA     |')
print('==='*15)
termo1 = int(input('PRIMEIRO TERMO: '))
razao = int(input('RAZÃO: '))
decimo = termo1 + (10 - 1) * razao
for c in range(termo1, decimo + razao, razao):
    print('{} '.format(c), end= '-> ')
print('FIM')
