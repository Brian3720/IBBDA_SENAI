'''
Crie um programa que retorne a tabuada de um número, e só pare quando o número digitado for 0000
'''

while True:
    numero = input('Digite um número: ')
    if numero == '0000':
        break
    for i in range(1,11):
        print(f'{numero} X {i} = {int(numero) * i}')