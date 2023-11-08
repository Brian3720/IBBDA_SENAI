#Escreva um programa que leia um tipo de dado e
#usando a função type(), retorne ao usuário, qual o tipo de dado informado

#Saída esperada:
#O dado é : <class ‘str’>

dado = float(input('Digita qualquer coisa: '))

oque = type(dado)

print(f'o dado foi {dado} e ele é {oque}')


