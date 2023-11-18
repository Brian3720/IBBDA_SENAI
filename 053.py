'''
Desafio
_________________________________________________________________________________________________
Crie um programa que vai gerar 10 números aleatórios e coloque em uma tupla.
Depois disso mostre a listagem de números gerados e indique o menor e o maior que estão na tupla
_________________________________________________________________________________________________

Exercicio:
Escreva uma tupla com 5 cores diferentes e print cada uma delas usando o for
'''
import time

cores = ('Vermelho', 'Azul', 'Verde', 'Roxo', 'Marrom')

for ele in cores:
    time.sleep(0.5)
    print(ele)

