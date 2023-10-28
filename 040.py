'''
Escreva um programa que leia um número n inteiro qualquer e mostra na tela os n primeiros
elementos de uma Sequência de Fibonacci
'''

numero = int(input('Quantos numeros da sequencia de fibonacci você gostarai de ver? '))
i = 0
anterior = 0
proximo = 0
contador = 0

while i < numero:
    contador += 1
    if i == 0:
        atual = 0

    if i == 1 or i == 2:
        atual = 1
        anterior = 0

    proximo = anterior + atual
    anterior = atual
    atual = proximo

    i += 1
    print(f'{contador}º número é = {atual}')