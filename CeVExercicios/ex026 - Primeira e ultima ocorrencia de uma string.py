frase = str(input('Digite uma frase: ')).strip()
frase = frase.upper()
print('A frase possui {} ás.'.format(frase.count('A')))
print('A primeira letra A aparece na posição {}.'.format(frase.find('A')+ 1))
print('A última letra A aparece na posição {}.'.format(frase.rfind('A')+1))
