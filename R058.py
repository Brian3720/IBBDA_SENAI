'''
Crie um programa onde serão informados diversos valores em uma lista. Caso o número já exista ele não será adicionado.
No final, serão exibidos todos os valores únicos em ordem crescente.
#### REVISAR ####
'''

def valores_unicos_ordenados(lista):
    # Usar um conjunto para armazenar valores únicos
    valores_unicos = set(lista)

    # Converter o conjunto de volta para uma lista e ordená-lo
    valores_unicos_ordenados = sorted(list(valores_unicos))

    return valores_unicos_ordenados


# Solicitar valores ao usuário até que ele deseje parar
valores = []
while True:
    valor = input("Digite um valor (ou 'sair' para encerrar): ")

    if valor.lower() == 'sair':
        break

    try:
        valor = float(valor)
        valores.append(valor)
    except ValueError:
        print("Digite um valor numérico válido.")

# Chamar a função para obter valores únicos ordenados
valores_unicos = valores_unicos_ordenados(valores)

# Exibir os resultados
print("\nValores únicos em ordem crescente:", valores_unicos)
