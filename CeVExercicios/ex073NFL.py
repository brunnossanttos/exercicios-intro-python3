tabela = ('Chiefs', 'Packers', 'Bills', 'Saints', 'Steelers', 'Seahawks', 'Titans', 'Buccaneers', 'Ravens', 'Browns',
          'Colts', 'Rams', 'Bears', 'WFT', 'Cardinals', 'Raiders', 'Dolphins', 'Vikings', 'Patriots', 'Chargers',
          '49ers', 'Giants', 'Cowboys', 'Broncos', 'Panthers', 'Lions', 'Bengals', 'Eagles', 'Texans', 'Falcons', 'Jets'
          , 'Jaguars')
print('*=*'*30)
print(f'A lista dos times em ordem alfabética é {sorted(tabela)}')
print('*=*'*30)
print(f'A classificação da NFL 2020 ficou assim: {tabela}')
print('*=*'*30)
print(f'Os times classificados para os playoffs são: {tabela[0:14]}')
print('*=*'*30)
print(f'{tabela[-1]} séra a primeira escolha do Draft 2021.')
print('*=*'*30)
print(f'O 49ers ficou na posição {tabela.index("49ers")- 1}')
