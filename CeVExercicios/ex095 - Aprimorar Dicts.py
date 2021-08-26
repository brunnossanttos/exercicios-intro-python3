dados = dict()
partidas = list()
time = list()
while True:
    dados.clear()
    dados['nome'] = str(input('Nome do jogador? '))
    dados['time'] = str(input(f'{dados["nome"]} joga em qual time? '))
    totalpartidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    partidas.clear()
    for c in range(1, totalpartidas + 1):
        partidas.append(int(input(f'Quantos gols {dados["nome"]} fez na {c}o partida? ')))
    dados['gols'] = partidas[:]
    dados['total'] = sum(partidas)
    time.append(dados.copy())
    while True:
        resp = str(input('Quer cadastrar outro jogador (S = SIM / N = NÃO)? ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('<< ERRO >> Por favor, use somente S ou N')
    if resp == 'N':
        break
print('-=' * 25)
print(' cod ', end='')
for i in dados.keys():
    print(f'{i :<15}', end='')
print()
print('-' * 50)
for k, v in enumerate(time):
    print(f'{k:>3}  ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
    print('-' * 50)
while True:
    levant = int(input('Deseja ver os dados de qual jogador? ( 999 para encerrar sessão) '))
    if levant == 999:
        break
    if levant >= len(time):
        print(f'<< ERRO >> Não existe jogador com o código {levant}')
    else:
        print(f' == LEVANTAMENTO DO JOGADOR {time[levant]["nome"]}  ==')
        for i, g in enumerate(time[levant]["gols"]):
            print(f' - - - No jogo {i + 1} fez {g} - - - ')
    print('-' * 50)
print(' = = = VOLTE SEMPRE = = = ')
