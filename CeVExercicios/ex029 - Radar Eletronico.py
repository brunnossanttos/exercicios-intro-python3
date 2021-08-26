velocidade = float(input('Qual a velocidade do automóvel:km/h '))
if velocidade <= 80:
    print('Parabéns, continue dirigindo com cuidado!!!')
else:
    multa = (velocidade - 80) * 7
    print('Você foi multado em R${:.2f}, por andar acima da velocidade permitida.'.format(multa))
