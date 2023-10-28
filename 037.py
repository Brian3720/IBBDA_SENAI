'''
Escreva um programa que peça ao usuário para adivinhar um número entre 1 e 10 e continue pedindo até que o usuário acerte o número.
E no final, retorne também a quantidade de tentativas necessárias.

'''
import random

numero_pc = random.randint(1,10)
contador = 0

print('Adivinhe um número entre 1 e 10')

resposta = int(input('chute um número: '))

while resposta != numero_pc:
    print(f'Sua resposta foi {resposta}, porém o número era {numero_pc}')
    contador += 1
    resposta = int(input(' tente novamente, qual seu chute?: '))
    numero_pc = random.randint(1,10)

print(f'Boa! Você conseguiu! seu chute foi {resposta} e o número que eu estava pensei era {numero_pc}'
      f'\nVocê precisou de {contador} tentativas')