from time import sleep
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o  segundo número: '))
escolha = 0
while escolha != 5:
    print('''
    [1] SOMAR 
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR''')
    escolha = int(input('>>>>>>>Digite o que deseja fazer: '))
    if escolha == 1:
        soma = num1 + num2
        print('A soma de {} com {}, é {}'.format(num1, num2, soma))
    elif escolha == 2:
        multiplicar = num1 * num2
        print('A multiplicação de {} por {}, é {}'.format(num1, num2, multiplicar))
    elif escolha == 3:
        maior = 0
        if num1 > num2:
            maior = num1
            print('O maior numero digitado foi {}.'.format(maior))
        else:
            maior = num2
            print('O maior numero digitado foi {}.'.format(maior))
    elif escolha == 4:
        num1 = int(input('Digite o novo valor: '))
        num2 = int(input('Digite o novo valor: '))
    elif escolha == 5:
        print('FINALIZANDO...')
        sleep(0.5)
    else:
        print('Opção inválida')
print('FIM DO PROGRAMA')
