'''
Crie um programa onde o usuário possa digitar sete letras, e cadastre em uma única lista, que mantenha separado as consoantes das vogais
'''

lista = [[], []]

for i in range(0,7):
    letra = input('Digite uma letra: ')
    if letra in 'aeiou':
        lista[0].append(letra)
    else:
        lista[1].append(letra)
print(f'As vogais são {lista[0]}'
      f'\nE as Consoantes são {lista[1]}')