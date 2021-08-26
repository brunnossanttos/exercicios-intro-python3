valortot = prodvalormil = menor = cont = 0
barato = ''
while True:
    print('---'*10)
    print('{:*^30}'.format(' LOJA DO BRUNÃO '))
    print('---'*10)
    nomeprod = str(input('Nome do Produto: '))
    preco = float(input('Preço:R$ '))
    valortot += preco
    if preco > 1000:
        prodvalormil += 1
    if cont == 1:
        menor = preco
        barato = nomeprod
    else:
        if preco < menor:
            menor = preco
            barato = nomeprod
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^30}'.format(' FIM DAS COMPRAS '))
print(f'O valor total dos produtos é R${valortot:.2f}.\n{prodvalormil} produtos com o valor maior que R$1000.'
      f'\nO produto mais barato é {barato}')
