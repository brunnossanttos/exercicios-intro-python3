num = int(input('Digite um número inteiro: '))
print('''Você quer converter para:
[0] Binário
[1] Octal
[2] Hexadecimal''')
escolha = int(input('Qual a sua escolha? '))
if escolha == 0:
    print('{} convertido para BINÁRIO  é igual a {}'.format(num, bin(num)[2:]))
elif escolha == 1:
    print('{} convertido pra OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif escolha == 2:
    print('{} convertido em HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção INVALIDA! Tente novamente.')
