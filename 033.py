'''
Escreva um programa que calcule a soma de todos os números múltiplos de 4 que são encontrados entre 1 até 500
'''

soma = 0

for i in range(1, 501):
    if i % 4 == 0:
        soma += i
print(f' A soma de 1 até 500 dos multiplos de 4 é {soma}')