anonasc = int(input('Qual o ano de nascimento do atleta? '))
idade = 2021 - anonasc
print('O atleta tem {} ano(s)'.format(idade))
if idade <= 9:
    print('ATLETA MIRIM')
elif 10 <= idade <= 14:
    print('ATLETA INFANTIL')
elif 15 <= idade <= 19:
    print('ATLETA JUNIOR')
elif 20 <= idade <= 25:
    print('ATLETA SENIOR')
elif idade > 25:
    print('ATLETA MASTER')
