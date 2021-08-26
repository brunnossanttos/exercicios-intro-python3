import moeda
p = float(input('Digite o preço: R$'))
t = int(input('Digite a taxa: '))
print(f'A metade de R${p} é {moeda.metade(p)}')
print(f'O dobro de R${p} é igual a {moeda.dobro(p)}')
print(f'O valor R${p} com aumento de {t}% é igual a {moeda.aumentar(p, t)}')
print(f'O valor R${p} com o desconto de {t}% é igual a {moeda.diminuir(p, t)}')
