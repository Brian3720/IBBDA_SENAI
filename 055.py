'''
Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois, deve mostrar para cada palavra, suas vogais
'''

tupla = ('Castigo', 'Amor', 'Crime', 'Sentido')

for palavra in tupla:
    print(f'\n{palavra}')
    for letra in palavra:
        if letra in 'aeiouAEIOU':
            print(letra, end=' ')
            