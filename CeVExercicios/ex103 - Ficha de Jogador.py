def ficha(jog='desconhecido', gol='0'):
    print(f'O jogador {jog} marcou {gol} gol(s).')


# Programa Principal
n = str(input('Nome do Jogador: '))
g = str(input('Gols marcados: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
