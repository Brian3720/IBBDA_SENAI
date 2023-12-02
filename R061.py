'''
Escreva um programa que crie uma lista vazia e permita que o usuário insira
números nessa lista até que ele digite um número negativo. Em seguida, exiba a lista na tela.
#### REVISAR ####
'''

# Criar uma lista vazia
lista_numeros = []

# Permitir que o usuário insira números na lista
while True:
    try:
        numero = float(input("Digite um número (ou um número negativo para encerrar): "))
        if numero < 0:
            break
        lista_numeros.append(numero)
    except ValueError:
        print("Digite um número válido.")

# Exibir a lista na tela
print("\nLista de números inseridos:", lista_numeros)

