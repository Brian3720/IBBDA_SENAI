'''
Escreva um programa que leia o raio de uma esfera, e calcule o seu volume e área.

V = (4/3) . π . r³
A = 4 . π . r²

Saída esperada:

Volume da Esfera: Y
Área da esfera: X
'''
import math

raio = int(input('Digite o raio da esfera: '))
volume = (4 / 3) * math.pi * raio ** 3

print(f'O volume da esfera de raio {raio} é {volume:.2f}')
