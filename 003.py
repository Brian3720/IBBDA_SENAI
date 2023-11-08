'''
Escreva um programa que leia o nome, e o sobrenome, CONCATENE em uma nova variável
nome completo, e retorne para o usuário
Saída esperada:
Seu nome completo é: Luis Tatin
'''

nome = input('Digite seu primeiro nome: ')
sobrenome = input('Digite seu sobrenome: ')

nomeInteiro = nome + ' ' + sobrenome

print(f'Seu nome: {nome}'
      f'\nSeu sobrenome: {sobrenome}'
      f'\nSeu nome inteiro: {nomeInteiro}')
