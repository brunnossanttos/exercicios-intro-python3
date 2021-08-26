resposta = 'S'
soma = cont = media = maior = menor = 0
while resposta in 'Ss':
    n = int(input('Digite um número: '))
    resposta = str(input('Quer continuar?[S/N] ')).strip()[0].upper()
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma / cont
print('Você digitou {} números e a média deles é {}'.format(cont, media))
print('O maior valor foi {} e o menor valor foi {}.'.format(maior, menor))
