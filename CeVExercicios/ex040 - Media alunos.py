n1 = float(input('Qual o valor da primeira nota? '))
n2 = float(input('Qual o valor da segunda nota? '))
m = (n1 + n2) / 2
print('Sua média é:{:.2f} '.format(m))
if m < 5:
    print('REPROVADO')
elif m >= 5 and m <= 6.9:
    print('RECUPERAÇÃO')
elif m >= 7:
    print('APROVADO')
