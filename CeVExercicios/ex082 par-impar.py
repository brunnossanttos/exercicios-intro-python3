lista = list()
pares = list()
impares = list()
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    resposta = str(input('Deseja digitar outro valor?{S/N} ')).strip().upper()
    if resposta == 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-=' * 30)
print(f'A lista completa é {lista}.')
print(f'A lista dos valores pares é {pares}')
print(f'A lista com os números ímpares é {impares}')
