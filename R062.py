'''
Escreva um programa que crie duas listas com 5 números cada uma e exiba a soma dos elementos correspondentes das duas listas.
Por exemplo, se as listas forem [1, 2, 3, 4, 5] e [5, 4, 3, 2, 1], o programa deve exibir [6, 6, 6, 6, 6].
#### REVISAR ####
'''

# Criar duas listas com 5 números cada
lista1 = [1, 2, 3, 4, 5]
lista2 = [5, 4, 3, 2, 1]

# Calcular a soma dos elementos correspondentes
soma_elementos = [a + b for a, b in zip(lista1, lista2)]

# Exibir as listas e a soma dos elementos correspondentes
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Soma dos elementos correspondentes:", soma_elementos)

