somaidade = 0
maioridade = 0
nomevelho = ''
qtsmulheres = 0
for p in range(1,5):
    print('-------- {}° PESSOA------------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo:(F/M) ')).strip()
    somaidade = idade + somaidade
    if p == 1 and sexo in 'Mm':
        maioridade = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        qtsmulheres += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridade, nomevelho))
print('A quantidade de mulheres com menos de 20 anos é {}.'.format(qtsmulheres))
