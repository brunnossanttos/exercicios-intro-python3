print('-=-'*20)
print('ANALISADOR DE TRIÂNGULOS')
print('-=-'*20)
r1 = float(input('Digite o cumprimento da reta 1: '))
r2 = float(input('Digite o cumprimento da reta 2: '))
r3 = float(input('Digite o cumprimento da reta 3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os valores digitados formam um triângulo', end=' ')
    if r1 == r2 == r3:
        print('EQUILÁTEREO')
    elif r1 == r2 and r1 != r3 or r1 == r3 and r1 != r2 or r2 == r3 and r2 != r1:
        print('ISÓSCELES')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
else:
    print('Os valores digitados NÃO formam um triângulo')
