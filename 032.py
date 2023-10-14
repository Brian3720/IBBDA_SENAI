'''
Escreva um programa que imprima todos os números pares entre dois números fornecidos pelo usuário.
'''

inicio = int(input("Digite o inicio do intervalo: "))
final = int(input("Digite o final do intervalo: "))

for i in range(inicio, final, + 1):
    if i % 2 ==0:
        print(f'{i} é Par')

