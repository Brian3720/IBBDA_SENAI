'''
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final mostre:

Qual é o total gasto na compra
Quantos produtos custam mais de R$1000,00
Qual é o produto mais barato
'''

reposta = ''
cont = 0
gasto_total = 0
maisDeMil = 0
menor = None
nome_prod_mais_barato = ''

while True:
    cont += 1
    produto = input(f' {cont}º Produto: ').strip().lower()
    preco = float(input(f'Digite o valor do {cont}º produto: R$'))
    gasto_total += preco

    if menor == None:
        menor = preco

    if preco <= menor:
        menor = preco
        nome_prod_mais_barato = produto

    if preco > 1000:
        maisDeMil += 1

    resposta = input('Deseja continuar? [S / N]').upper()
    if resposta == 'N':
        break


print(f'\nO gasto total é {gasto_total}'
      f'\nTivemos {maisDeMil} produtos que custam mais de R$1,000.00'
      f'\nO produto mais barato é: {nome_prod_mais_barato}')