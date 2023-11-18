'''
Usando tuplas, leia um número de 0 a 15, e retorne esse número escrito por extenso
'''



numeros = {0: 'Zero',
           1: 'Um',
           2: 'Dois',
           3: 'Três',
           4: 'Quatro',
           5: 'Cinco',
           6: 'Seis',
           7: 'Sete',
           8: 'Oito',
           9: 'Nove',
           10: 'Dez',
           11: 'Onze',
           12: 'Doze',
           13: 'Treze',
           14: 'Quatorze',
           15: 'Quinze'}

numero = int(input('Digite um número de 0 a 15: '))

print(numeros[numero])

