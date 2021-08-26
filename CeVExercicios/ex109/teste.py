from ex109 import moeda
p = float(input('Digite o preço: R$'))
t = int(input('Digite a taxa: '))
while True:
    f = str(input('Deseja o valor formatado?(S/N) ')).strip().upper()
    if f in 'SN':
        break
    else:
        print('Resposta Inválida. Use somente S ou N.')
if f == 'S':
    fvalor = True
else:
    fvalor = False
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, fvalor)}')
print(f'O dobro de {moeda.moeda(p)} é igual a {moeda.dobro(p, fvalor)}')
print(f'O valor {moeda.moeda(p)} com aumento de {t}% é igual a {moeda.aumentar(p, t, fvalor)}')
print(f'O valor {moeda.moeda(p)} com o desconto de {t}% é igual a {moeda.diminuir(p, t, fvalor)}')
