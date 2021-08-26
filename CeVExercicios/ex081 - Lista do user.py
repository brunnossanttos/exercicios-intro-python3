lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    resposta = str(input('Deseja acrescentar mais um número?{S/N} ')).strip().upper()
    if resposta == 'N':
        break
print('=-'*30)
print(f'Você digitou {len(lista)} valores.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente é {lista}')
if 5 in lista:
    print('O valor 5, faz parte da lista.')
else:
    print('O valor não vai parte da lista.')
