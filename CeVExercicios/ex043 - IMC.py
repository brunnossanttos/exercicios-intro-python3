peso = float(input('Qual o seu peso? (kg)'))
altura = float(input('Qual a sua altura? (m)'))
imc = peso / (altura ** 2)
print('Seu IMC é igual a {:.1F}'.format(imc), end= ' ')
if imc < 18.5:
    print('ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print(' PESO IDEAL')
elif 25 <= imc < 30:
    print('SOBREPESO. Tome mais cuidado!!!')
elif 30 <= imc < 40:
    print('OBESIDADE!!! Procure um médico')
else:
    print('OBESIDADE MORBIDA. VOCÊ PRECISA DE AJUDA URGENTE')
