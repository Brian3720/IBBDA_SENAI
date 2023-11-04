'''
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa
vai informar quantas cédulas de cada valor serão entregues.

Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1
'''


valor = int(input('digite o valor a ser sacado: '))

cedulas_50 = valor // 50
valor = valor % 50

cedulas_20 = valor // 50
valor = valor % 50

cedulas_10 = valor // 50
valor = valor % 50

cedulas_1 = valor // 50
valor = valor % 50

print(f'A quantidade de notas de 50: {cedulas_50}'
      f'\nA quantidade de notas de 20: {cedulas_20}'
      f'\nA quantidade de notas de 10: {cedulas_10}'
      f'\nA quantidade de notas de 1: {cedulas_1}')
