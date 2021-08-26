distancia = float(input('Qual a distância da sua viagem?km/ '))
if distancia <= 200:
    valor = distancia * 0.5
    print('A sua passagem custará R${:.2f}'.format(valor))
else:
    valor = distancia * 0.45
    print('A sua passagem custará R${:.2f}'.format(valor))
