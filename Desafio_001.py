'''
Escreva um programa que execute o cálculo da Função
horária da posição no MRUV, e retorne de acordo com o
tempo informado pelo usuário

Saída esperada:

A posição do objeto no tempo x é de y (m)
'''

def calcular_posicao_mruv(S0, V0, a, t):
    S = S0 + V0 * t + 0.5 * a * t**2
    return S

# Solicitar informações ao usuário
S0 = float(input("Informe a posição inicial (m): "))
V0 = float(input("Informe a velocidade inicial (m/s): "))
a = float(input("Informe a aceleração (m/s²): "))
t = float(input("Informe o tempo (s): "))

# Calcular a posição usando a função
posicao = calcular_posicao_mruv(S0, V0, a, t)

# Exibir o resultado
print(f"A posição do objeto no tempo {t} é de {posicao:.2f} (m)")

#font: GPT 3
