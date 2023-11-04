'''
Crie um programa que leia vários números inteiros. O programa só vai parar quando o usuário digitar 0000.
No final mostre quantos números foram digitados e qual a soma entre eles (desconsiderando o flag)
'''

soma = 0
quant_numeros = 0

while True:
    numero = (input('Digite um numero: '))

    if numero == '0000':
        break

    soma += int(numero)
    quant_numeros += 1

print(f'\n\nPrograma finalizado.'
      f'\nVocê digitou {quant_numeros} números'
      f'\nA soma dos números é {soma}')