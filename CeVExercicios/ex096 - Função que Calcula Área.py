def area(lar, comp):
    # Calcula área de um terreno
    a = lar * comp
    print(f'A área de um terreno {lar}x{comp} é de {a}m²')


# Programa Principal
print('   CONTROLE DE TERRENOS')
print('-' * 25)
l = float(input('LARGURA:(m) '))
c = float(input('COMPRIMENTO:(m) '))
area(l, c)
