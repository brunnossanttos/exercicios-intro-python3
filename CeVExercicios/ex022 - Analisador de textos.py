nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando o seu nome...')
print('O seu nome com todas as letras maiusculas: ', nome.upper())
print('O nome com todas as letras minusculas: ', nome.lower())
print('Seu nome tem {} letras no total'.format(len(nome) - nome.count(' ')))
print('O seu primeiro tem {} letras: '.format(nome.find(' ')))