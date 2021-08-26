maior = homen = mulhermaior = 0
while True:
    print('---' * 10)
    print('CADASTRO DE UMA PESSOA')
    print('---'*10)
    idade = int(input('IDADE: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('SEXO:[M/F] ')).strip().upper()[0]
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homen += 1
    if idade < 20 and sexo == 'M':
        mulhermaior += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer contunuar?[S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'Total de pessoas maior de 18 anos: {maior}\nAo todo foi {homen} homen(s) cadastrado(s)\nE temos {mulhermaior} '
      f'mulhere(s) com menos de 20 anos')
