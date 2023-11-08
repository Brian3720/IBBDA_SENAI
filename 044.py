'''
Crie um programa para jogar par ou ímpar com o usuário, e só pare quando perder.
Ao final deve mostrar a quantidade de vitórias
'''

import random


vitorias = 0
while True:
    pc = random.randint(0,10)
    jogador = int(input('Digite um número entre 0 e 10: '))
    escolha = input('Par [P] ou Impar [I]: ').upper()

    if pc + jogador % 2 == 0 and escolha == 'P':
        print(f'Você ganhou'
              f'\nComputador jogou {pc}'
              f'\nVocê jogou {jogador}'
              f'\n')
        vitorias += 1

    elif pc + jogador % 2 != 0 and escolha == 'I':
        print(f'Você ganhou'
              f'\nComputador jogou {pc}'
              f'\nVocê jogou {jogador}'
              f'\n')
        vitorias += 1

    else:
        print(f'Você perdeu ;-;'
              f'\nComputador jogou {pc}'
              f'\nVocê jogou {jogador}'
              f'\n'
              f'\n'
              f'\nO número de vitórias seguidas foram de {vitorias}')