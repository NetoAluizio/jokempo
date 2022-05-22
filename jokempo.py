#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random


nomeJogador = input('Qual o seu nome? ')
escolhasRobot = [1, 2, 3]
print('Olá', nomeJogador, '!', 'Meu nome e Robot, prazer em conhecê-lo')
print('Antes de começar, vou lhe passar algumas informações:')
print('Escolha uma opção (1, 2, 3 ou 4).')
print('1-Pedra')
print('2-Papel')
print('3-Tesoura')
print('4-Sair')

continuar = 1

while (continuar == 1):
    
    jogador = int(input('Sua escolha: '))
    robot = random.choice(escolhasRobot)
    if (1 <= jogador <= 3) and (1 <= robot <= 3):
        if (jogador == robot):
            if (jogador == 1):
                print('Sua jogada -> Pedra')
                print('Minha jogada -> Pedra')
            elif (jogador == 2):
                print('Sua jogada -> Papel')
                print('Minha jogada -> Papel')
            else:
                print('Sua jogada -> Tesoura')
                print('Minha jogada -> Tesoura')
            print('Empate!')
        elif (jogador - robot == -2) or (jogador - robot == 1):
            if (jogador == 1):
                print('Sua jogada -> Pedra')
                print('Minha jogada -> Tesoura')
            elif (jogador == 2):
                print('Sua jogada -> Papel')
                print('Minha jogada -> Pedra')
            else:
                print('Sua jogada -> Tesoura')
                print('Minha jogada -> Papel')
            print('Parabéns, você ganhou!')
        else:
            if (jogador == 1):
                print('Sua jogada -> Pedra')
                print('Minha jogada -> Papel')
            elif (jogador == 2):
                print('Sua jogada -> Papel')
                print('Minha jogada -> Tesoura')
            else:
                print('Sua jogada -> Tesoura')
                print('Minha jogada -> Pedra')
            print('Venci! Devo comemorar?')
    elif (jogador == 4):
        print('Ok, até a próxima')
        break
    else:
        print('Hum! Você digitou algo errado!')
        
    continuar = int(input('Vamos outra rodada? Digite 1 para jogar e 4 para sair: '))
    if (continuar <= 3):
        print('Escolha uma opção (1, 2, 3 ou 4).')
        print('1-Pedra')
        print('2-Papel')
        print('3-Tesoura')
        continue
    else:
        print('Ok, até a próxima!')
        break


# In[ ]:




