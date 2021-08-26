from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1, 3):
    ano = int(input('Digite o {}° ano de nascimento: '.format(c)))
    idade = atual - ano
    if idade < 21:
        menor += 1
    elif idade >= 21:
        maior += 1
print('Dos anos digitados, somente {} pessoas são menores de idade'.format(menor))
print('Dos anos digitados, somente {} pesssoas são maiores de idade'.format(maior))
