'''
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
Saída esperada:

A dobro de 9 é : 18
A triplo de 9 é : 27
A raiz quadrada de 9 é : 3
'''

import math

numero = int(input('Digite um número: '))

dobro = numero * 2

trip = numero * 3

raiz = math.sqrt(numero)

print(f'numero: {numero}'
      f'\ndobro: {dobro}'
      f'\ntriplo: {trip}'
      f'\nRaiz quadrada: {raiz}')
