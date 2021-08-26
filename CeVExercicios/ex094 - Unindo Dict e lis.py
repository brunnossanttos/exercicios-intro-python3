dados = dict()
galera = list()
soma = media = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo:[M/F] ')).upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('ERRO. Use somente M ou F.')
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    galera.append(dados.copy())
    while True:
        resp = str(input('Deseja cadastrar outra pessoa?[S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('Erro. Use somente M ou F')
    if resp == 'N':
        break
print(f'a) Você cadastrou {len(galera)} pessoas.')
media = soma / len(galera)
print(f'b) A média de idade das pessoas cadastradas é igual a {media:5.2f} anos.')
print('c) As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f' {p["nome"]} ')
print('As pessoas cadastradas com idade acima da média foram: ', end='')
for p in galera:
    if p['idade'] >= media:
        print()
        for k, v in p.items():
            print(f' -- {k} = {v}')
        print()
print()
