print('=-='*15)
print('         ALISTAMENTO MILITAR')
print('-=-'*15)
nome = str(input('Qual o seu nome? '))
datanasc = int(input('Em que ano você nasceu? '))
idade = 2021 - datanasc
falta = 18 - idade
anolista = 2021 + falta
jaalistou = datanasc + 18
if idade == 18:
    print('Você deve procurar a JUNTA MILITAR mais próxima e fazer o alistamento')
elif idade < 18:
    print('Falta {} ano(s) para seu alistamento, que será no ano de {}'.format(falta, anoalista))
else:
    print('Caso você ainda não tenha se alistado no ano {} ou posteriomente a isso, procure a JUNTA MILITAR o mais rápido possivél'.format(jaalistou))
