'''
Crie um algoritmo que leia um salário e simule um reajuste positivo de 60%.
Saída esperada:

O salário de 6000 com o reajuste de 60% será de : 9600
'''

salario = float(input('Qual seu salario: '))

reajuste = (30/100) * salario

salarioNovo = salario + reajuste

print(f'O seu salario de R${salario} teve um reajuste de '
      f'{reajuste}%; O salario agora passa a ser R${salarioNovo:.2f}')

