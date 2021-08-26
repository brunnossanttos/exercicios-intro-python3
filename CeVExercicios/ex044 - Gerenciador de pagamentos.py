print('{:.^40}'.format('LOJAS DO BRUNÃO'))
preço = float(input('Digite o valor das compras: R$'))
print('''
Forma de pagamento
[1] à vista dinheiro/cheque: 10% de desconto.
[2] à vista no cartão: 5% de desconto.
[3] em até 2x no cartão: preço formal
[4] 3x ou mais no cartão: 20% de juros''')
pagto = int(input('Digite a forma de pagamento: '))
print('O valor das suas compras é {}'.format(preço), end=' ')
if pagto == 1:
    total = preço - (preço * (10 / 100))
    print('o total a ser pago é de {:.2f} com desconto de 10%'.format(total))
elif pagto == 2:
    total = preço - (preço * (5 / 100))
    print('o total a ser pago é de {:.2f} com desconto de 5%'.format(total))
elif pagto == 3:
    total = preço / 2
    print('que serão pagos em 2x de R${:.2f} Sem juros'.format(total))
elif pagto == 4:
    parcelas = int(input('Em quantas parcelas você quer dividir? '))
    total = preço + (preço * (20 / 100))
    valorparcelas = total / parcelas
    print('o total a ser pago é de {:.2f} em {} meses de {:.2f}'.format(total, parcelas, valorparcelas))
