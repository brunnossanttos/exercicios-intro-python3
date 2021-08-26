print('-=-'*15)
print('       BANCO SUA CASA SUA VIDA')
print('-=-'*15)
nome = str(input('Qual o seu nome: '))
sal = float(input('Qual o valor do seu salário, {}? R$'.format(nome)))
valorcasa = float(input('Olá {}, qual o valor da casa que deseja comprar? R$'.format(nome)))
parcelas = int(input('Em quantos anos deseja pagar a casa: '))
totalparcelas = parcelas * 12
valorparcela = valorcasa / totalparcelas
if valorparcela > (sal * 0.3):
    print('Infelizmente o emprestimo não foi aprovado. Pois o valor da parcela {:.2f} excendeu 30% do seu salário, {}'.format(valorparcela,nome))
else:
    print('Emprestimo aprovado! Parabéns! O valor da parcela é: {}, será pago em {} meses ou {} anos'.format(valorparcela, totalparcelas, parcelas))
