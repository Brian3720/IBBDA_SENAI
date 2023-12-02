'''
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final mostre a matriz na tela, com a formatação correta
'''

matriz = [[],[],[]]

try:
    for i in range(0, 3):
        for ele in range(0, 3):
            numero = int(input('Digite um número: '))
            matriz[i].append(numero)

    print(f'A matriz é : {matriz}')
    for linha in matriz:
        print(linha)

except ValueError:
    print('Digite apenas números')