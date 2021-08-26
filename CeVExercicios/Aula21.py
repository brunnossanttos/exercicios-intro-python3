# Parâmetros Opcionais
# def somar(a=0, b=0, c=0):
#     s = a + b + c
#     print(f'A soma vale {s}.')
#
#
# somar(4, 8, 3)
# somar(5, 3)
# somar()
#
# Escopo de Variáveis
# def teste():
#      global n
#      x =8
#      print(f'Na função teste, n vale {n}.')
#      print(f'Na função teste, x vale {x}.')
#
#
# Programa Principal
# n = Escopo Global, x = Escopo Local
# n = 2
# print(f'No programa principal, n vale {n}')
# teste()
#
#  Retornando Valores
# def somar(a=0, b=0, c=0):
#     s = a + b + c
#     return s
#
#
# r1 = somar(3, 2, 5)
# r2 = somar(5, 1)
# r3 = somar(10,5)
# print(f'Meus cáculos deram {r1}, {r2} e {r3}')
# def fatorial(num=1):
#     f = 1
#     for c in range(num, 0, -1):
#         f *= c
#     return f
#
#
# n = int(input('Digite um número: '))
# print(f'O fatorial de {n} é igual a {fatorial(n)}')
# f1 = fatorial(5)
# f2 = fatorial(4)
# f3 = fatorial()
# print(f'Os resultados são {f1}, {f2} e {f3}')
def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
print(par(num))
if par(num):
    print('É par!')
else:
    print('É impar!')
