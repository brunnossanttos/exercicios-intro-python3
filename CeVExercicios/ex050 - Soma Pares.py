soma = 0
cont = 0
for c in range(1,7):
    valor = int(input('Digite o {}° valor: '.format(c)))
    if valor % 2 == 0:
        soma += valor
        cont += 1
print('Você informou {} valor(es) par(es), a soma do(s) valor(es) par(es) digitado(s) é {}'.format(cont, soma))
