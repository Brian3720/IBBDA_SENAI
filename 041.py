'''
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre
a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores
'''

pergunta = ''
soma = 0
maior = 0
menor = 0
contador = 0

while pergunta != 'N':
    numero = int(input('Digite um número: '))
    pergunta = input('Deseja continuar? [S/N]').upper().strip()
    soma = soma + numero

    if contador == 0:
        maior = numero
        menor = numero
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

    contador += 1

media = soma / contador
print(f'O maior é {maior}'
      f'\nO menor é {menor}'
      f'\nA média é {media}')
