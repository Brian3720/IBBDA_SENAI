'''
Escreva um programa que leia o
Nome, idade e sexo de 4 pessoas. No final mostre:

A média de idade do grupo
Qual é o homem mais velho
Quantas mulheres têm menos de 20 anos
'''

nome = []
sexo = []
idade = []

for i in range(1, 5, +1):
    print("cadastro de cliente")
    nome.append(input("digite um nome: "))
    sexo.append(input("Masculino / Feminino?: ").lower())


print(nome)
