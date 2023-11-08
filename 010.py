'''
Escreva um programa que leia um tipo de dado e
usando a método .isnumeric(), retorne ao usuário

Saída esperada:

O dado informado é número?
	TRUE / FALSE
'''

dado = input('Digite um dado qualquer: ')

oque = dado.isnumeric()

print(f'dado é {dado} ele número?: {oque}')

