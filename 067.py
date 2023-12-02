'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear
6 números entre 1 a 60 para cada jogo, cadastrando tudo em uma lista composta
'''
from random import randint

try:
    pergunta = int(input('Quantos jogos deseja gerar? '))
    palpites = []
    lista_sec = []

    for i in range(0, pergunta):
        while len(lista_sec) != 6:
            numero = randint(1,60)
            if numero not in lista_sec:
                lista_sec.append(numero)
        palpites.append(lista_sec[:])
        lista_sec.clear()

    for palpite in palpites:
        print(sorted(palpite))

except ValueError:
    print('Aceitamos apenas números')
