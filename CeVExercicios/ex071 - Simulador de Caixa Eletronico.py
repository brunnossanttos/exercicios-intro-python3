print('==='*10)
print('{:*^30}'.format(' BANCO DO BRUNÃO '))
print('==='*10)
saque = float(input('QUAL O VALOR DESEJA SACAR? R$'))
total = saque
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('==='*10)
print('{:*^30}'.format(' VOLTE SEMPRE AO BB '))
