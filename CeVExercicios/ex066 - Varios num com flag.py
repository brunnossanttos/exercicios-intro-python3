cont = soma = 0
while True:
    n = int(input('Digite um número:[999 PARA PARAR] '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Você digitou {cont} números, e a soma deles é {soma}.')
