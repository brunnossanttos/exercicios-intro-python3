sal = float(input('Qual o seu salário atual? '))
if sal >= 1250:
    saln = sal * 0.1 + sal
    print('Seu novo salário é \033[1;31;40mR${:.2f}\033[m'.format(saln))
else:
    saln = sal * 0.15 + sal
    print('Seu novo salário é R${:.2f}'.format(saln))
