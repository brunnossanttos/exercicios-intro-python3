ano = int(input('Qual o ano você deseja analisar?'))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é BISSEXTO'.format(ano))
else:
    print('{} não é BISSEXTO'.format(ano))
