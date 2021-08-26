alunos = dict()
alunos['nome'] = str(input('Nome: '))
alunos['media'] = float(input('Média: '))
print('=-' * 25)
print(f'Nome do aluno {alunos["nome"]}.')
print(f'A média do {alunos["nome"]} é {alunos["media"]}')
if alunos['media'] >= 7.5:
    print('Situação: APROVADO')
elif 5 <= alunos['media'] < 7.4:
    print('Situação: RECUPERAÇÃO')
elif alunos['media'] <= 4.9:
    print('Situação: REPROVADO')
