'''
Escreva um programa que leia, o nome, idade, e cidade de nascimento e retorne para o usuário

Saída esperada:

Meu nome é Luis Tatin, tenho 22 anos e nasci em São Bernardo do campo
'''

nome = input('Digite seu primeiro nome: ').strip()
sobrenome = input('Digite aqui seu sobrenome: ').strip()
cidade = input('Digite sua cidade: ').strip()
idade = int(input('Digite sua idade: ').strip())

print(f'Meu nome é {nome} {sobrenome}, tenho {idade} anos e nasci em {cidade}')
