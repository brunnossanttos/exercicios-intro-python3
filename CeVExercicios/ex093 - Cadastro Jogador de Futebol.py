dados = dict()
partidas = list()
dados['nome'] = str(input('Nome do jogador: '))
totpartidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for c in range(1, totpartidas + 1):
    partidas.append(int(input(f'Quantos gols na partida {c}? ')))
dados['gols'] = partidas[:]
dados['total'] = sum(partidas)
print('=-' * 25)
print(dados)
print('-=' * 25)
for k, v in dados.items():
    print(f' -- O campo {k} tem o valor: {v}.')
print('=-' * 25)
print(f'O jogador {dados["nome"]} jogou {len(dados["gols"])} partidas.')
for i, v in enumerate(dados['gols']):
    print(f'    => Na partida {i + 1}, fez {v} gols.')
print(f'Foi um total de {dados["total"]} gols')
