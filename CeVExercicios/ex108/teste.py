from ex108 import moeda
p = float(input('Digite o preço: R$'))
t = int(input('Digite a taxa: '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é igual a {moeda.moeda(moeda.dobro(p))}')
print(f'O valor {moeda.moeda(p)} com aumento de {t}% é igual a {moeda.moeda(moeda.aumentar(p, t))}')
print(f'O valor {moeda.moeda(p)} com o desconto de {t}% é igual a {moeda.moeda(moeda.diminuir(p, t))}')
