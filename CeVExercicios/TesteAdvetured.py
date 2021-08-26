# from random import randint
from time import sleep
print('=-'*15)
nome = str(input('Qual o seu nome? '))
sleep(2)
print(f'Vamos jogar, {nome}?')
sleep(1)
print(f'Você recebeu dois convites para sexta à noite:\n[1] De: Alice.\n Ei? {nome}, vai rolar a maior festa hoje, na '
      f'casa da minha prima vamos??? Vai ser DEMAIS. Conto com a sua presença.')
sleep(3)
print(f'[2] De: Dante.\nEi, tu viu que Donnie Darko Remasterizado estar em cartaz??? Não vamos perder essa por nada, '
      f'certo?')
sleep(3)
escolha1 = int(input('Você deseja ir a festa[1] ou ao cinema[2]? '))
sleep(2)
if escolha1 == 1:
      print('Vamos para festa!!!!\nDIA DA FESTA')
      sleep(3)
      print('*MENSAGEM DE ALICE*')
      sleep(3)
      print('Eiii, às 21h passo na sua casa, ok? A noite promete!!!!')
      sleep(3)
      print('Responda com:\n[1] = Estou super animado, mal consigo esperar. Até logo!!!\n[2] = Não estou muito animado,'
            'vamos ficar em casa, assistir um filme, sei lá? O que acha? ')
      sleep(2)
      mensagem1 = int(input('Qual resposta você escolhe?[1/2] '))
      if mensagem1 == 1:
            print('Alice: VAI SER INCRIVÉL!!! ;)')
            print('22h')
            sleep(2)
            print('Nada da Alice aparecer\n*Mensagem de Dante*\nDante: Cara o filme está DEMAIS. Você perdeu, coisa'
                  'mais linda. Espero que a festa valha a pena, otário. HAHAHA')
            sleep(2)
            print('BI BIIIIIIIII')

      else:
            print(f'Poxa {nome}, vamos, vai ser divertido. Na proxima semana, eu deixo vc escolher oque iremos, fazer,'
                  f' ok?')
            sleep(2)
            mensagem2 = str(input('Realmente quer in na festa?[S/N]')).strip().upper()
            if mensagem2 == 'S':
                  print('Ok, Alice. Vamos nessa!')
            else:
                  print('Não, acho melhor não...')
                  sleep(2)
                  print('Alice: Ok... Tchau.')
else:
      print('Vamos ao cinema')
