ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota I: '))
    nota2 = float(input('Nota II: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar?(S/N) ')).strip().upper()
    if resp == 'N':
        break
print('=-' * 15)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-' * 30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('=-' * 15)
    opc = int(input('Deseja ver a nota de qual aluno?[999 interrompe] '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de  {ficha[opc][0]} são {ficha[opc][1]}')
print('Volte sempre')