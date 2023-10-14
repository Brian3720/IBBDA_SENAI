'''
Escreva um programa que imprima a tabuada de um número fornecido pelo usuário.
'''
import time
print("ESCOLHA UMA TABUADA")
numero = int(input("digite um numero: "))

for contador in range (1,11):
    print(f'| {numero} X {contador} = {numero * contador} |')


'''
multiplicador = 0
for multiplicador in range (multiplicador,11):
    multiplicador = multiplicador
    resultado = numero * multiplicador
    print(f'{multiplicador} X {numero} = {resultado}')
    time.sleep(0.45)
'''
