tabela = ('Palmeiras', 'Bragantino', 'Athletico-PR', 'Fortaleza', 'Bahia', 'Atlético-MG', 'Santos', 'Atlético-GO',
          'Flamengo', 'Ceará', 'Fluminense', 'Juventude', 'Corinthians', 'Internacional', 'América-MG', 'Sport',
          'Cuiabá', 'São Paulo', 'Chapecoense', 'Grêmio')
print('==='*30)
print(f'A classificação do campeonato é {tabela}')
print('==='*30)
print(f'Os times que estariam classificados para a Libertadores 2022 são: {tabela[0:5]}')
print('==='*30)
print(f'Os times que estariam reibaxados para a Série B 2022 são: {tabela[-4:]}')
print('==='*30)
print(f'Lista dos times em ordem alfabética: {sorted(tabela)}')
print('==='*30)
print(f'A Chapecoense está na {tabela.index("Chapecoense")+ 1} posição')
