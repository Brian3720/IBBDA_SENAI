'''
Escreva um programa que converta real para o Franco Congolês
Saída esperada:

10,00 reais, equivalem a 5052,00 Francos Congoleses
'''

fc = 526.07
real = float(input(f'Digite a quantidade de real que deseja converter para FC: '))
convercao = real * fc

print(f'{real} reais, equivalem a {convercao:.2f} Francos congoleses')
