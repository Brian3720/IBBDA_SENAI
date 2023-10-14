'''
Escreva um programa que leia 10 números, se for ímpar deve ser descartado, se não, deve ser agregado a uma soma
'''

for i in range(1,11):
    Numero = int(input('Digite seu número'))
    if Numero % 2 == 0:
        soma += Numero

print(f'A soma dos pares é {soma}')
