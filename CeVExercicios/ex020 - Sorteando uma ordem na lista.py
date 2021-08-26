import random
n1 = str(input("Digite o nome do aluno: "))
n2 = str(input("Digite o nome do aluno: "))
n3 = str(input("Digite o nome do aluno: "))
n4 = str(input("Digite o nome do aluno: "))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print("A ordem de apresentação será: ")
print(lista)

'''from random import shuffle
jogador1 = str(input("Digite o nome do primeiro time: "))
jogador2 = str(input("Digite o nome do segundo time: "))
jogador3 = str(input("Digite o nome do terceiro time: "))
jogador4 = str(input("Digite o nome do quarto time: "))
lista = [jogador1, jogador2, jogador3, jogador4]
shuffle(lista)
print("Os confrontos serão entre: ")
print(lista)'''
