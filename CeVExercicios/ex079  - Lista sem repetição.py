listanum = []
while True:
    n = int(input('Digite um valor: '))
    if n not in listanum:
        listanum.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor já existente... Não será adicionado')
    resposta = str(input('Deseja digitar mais um valor?[S/N] ')).strip().upper()
    if resposta == 'N':
        break
print('-='*30)
listanum.sort()
print(f'Os valores digitados em ordem crescente é\n{listanum}')
