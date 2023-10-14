'''
Escreva um programa que leia o
Nome, idade e sexo de 4 pessoas. No final mostre:

A média de idade do grupo
Qual é o homem mais velho
Quantas mulheres têm menos de 20 anos
'''

Soma_idade = 0
Idade_Homem_Mais_Velho = 0
Nome_Homem_Mais_Velho = ''
Quant_Mulheres_Menor_20_anos = 0

for i in range(1, 5):

    print('-----------------------------------')
    nome = input('Digite um nome: ')
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo [M], [F]: ')


    Soma_idade += idade

    if sexo == 'M' and Idade_Homem_Mais_Velho < idade:
        Idade_Homem_Mais_Velho = idade
        Nome_Homem_Mais_Velho = nome

    if sexo == 'F' and idade < 20:
        Quant_Mulheres_Menor_20_anos += 1

Media_idade = Soma_idade / 4

print(f'A média de idade dos grupos é {Media_idade}'
      f'\nO homem mais velho é {Nome_Homem_Mais_Velho} e a idade dele é {Idade_Homem_Mais_Velho}'
      f'\nExistem {Quant_Mulheres_Menor_20_anos} menores de 20 anos')
