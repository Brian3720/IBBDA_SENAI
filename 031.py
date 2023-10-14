'''
Escreva um programa que verifique se uma frase é um palíndromo.
'''
palavra = input("Digite uma palavra: ")

compatibilidade = 0

for i in range (0, len(palavra)):
    if palavra[i] == palavra[-i -1]:
        compatibilidade += 1

if compatibilidade == len(palavra):
    print(f'{palavra} é palindromo')
else:
    print("Não é palindromo")