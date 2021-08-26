galera = list()
pessoas = dict()
soma = media = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo:[M/F] ')).upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO. Por favor use somente M ou F')
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    galera.append(pessoas.copy())
    while True:
        resp = str(input('Quer continuar?[S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO. Por favor use somente S ou N')
    if resp == 'N':
        break
print('-=' * 25)
print(f'a) Foram cadastradas {len(galera)} pessoas')
media = soma / len(galera)
print(f'b) A média de idade é {media:5.2f} anos')
print('c) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f' {p["nome"]} ', end='')
print()
print(f'd) Lista de pessoas com idade acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('         ', end='')
        for k, v in p.items():
            print(f' {k}  =  {v};', end='')
        print()
print('<<< ENCERRADO >>>')
