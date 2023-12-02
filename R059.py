'''
Escreva um programa que crie uma lista com os números de 1 a 10 e, em seguida, exiba apenas os números ímpares da lista.
#### REVISAR ####
'''

# Criar uma lista com os números de 1 a 10
numeros = list(range(1, 11))

# Exibir apenas os números ímpares da lista
numeros_impares = [numero for numero in numeros if numero % 2 != 0]

# Exibir os resultados
print("Lista completa:", numeros)
print("Números ímpares:", numeros_impares)


