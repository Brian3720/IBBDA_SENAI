'''
Faça um programa com uma função maior e menor, que leia uma lista com 5 valores informados pelo usuário
e retorne esses valores e a posição deles.

#### REVISAR ####
'''

def encontrar_maior_menor(lista):
    maior = menor = lista[0]
    posicao_maior = posicao_menor = 0

    for i in range(1, len(lista)):
        if lista[i] > maior:
            maior = lista[i]
            posicao_maior = i
        elif lista[i] < menor:
            menor = lista[i]
            posicao_menor = i

    return maior, posicao_maior, menor, posicao_menor

# Solicitar 5 valores ao usuário
valores = []
for i in range(5):
    valor = float(input(f"Digite o {i + 1}º valor: "))
    valores.append(valor)

# Chamar a função para encontrar maior e menor valor, junto com suas posições
maior, posicao_maior, menor, posicao_menor = encontrar_maior_menor(valores)

# Exibir os resultados
print("\nValores informados:", valores)
print(f"O maior valor é {maior} na posição {posicao_maior + 1}")
print(f"O menor valor é {menor} na posição {posicao_menor + 1}")



