# teste = list()
# teste.append('Bruno')
# teste.append(21)
# galera = list()
# galera.append(teste[:])
# teste[0] = 'Tony'
# teste[1] = 56
# galera.append(teste[:])
# print(galera)
# galera = [['George', 28], ['Warner', 27], ['Samuel', 24], ['Bosa', 23]]
# print(galera[0])
# for p in galera:
#     print(p[0])
galera = list()
dados = list()
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
print(galera)
