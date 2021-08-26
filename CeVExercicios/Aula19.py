# print(pessoas.values()) pega somente os valores
# print(pessoas.keys()) pega chaves oq seria o valor númerico
# print(pessoas.items()) pega tudo
# pessoas = {'nome': 'Bruno', 'sexo': 'M', 'idade': 21}
# print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
# '''Dicionario dentro de uma lista'''
# brasil = []
# estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
# brasil.append(estado1)
# brasil.append(estado2)
# print(brasil)
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
