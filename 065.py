'''
Faça um programa que leia o nome e o QI de várias pessoas, guardando tudo e uma lista.
No final mostre:

Quantas pessoas foram cadastradas
Uma listagem com as pessoas com o maior QI
Uma listagem com as pessoas de menor QI

'''

lista = [[],[]]

try:
    while True:
        nome = input('Digite o nome (fim para sair): ')
        if nome == 'fim':
            break
        lista[0].append(nome)

        qi = int(input('Digite o QI: '))
        lista[1].append(qi)

    print(f'Foram cadastradas {len(lista[1])} pessoas')

    #Maior
    maior_qi = max(lista[1])
    posicao_maior_qi = lista[1].index(maior_qi)
    nome_maior_qi = lista[0][posicao_maior_qi]

    #Menor
    menor_qi = min(lista[1])
    posicao_menor_qi = lista.index(menor_qi)
    nome_menor_qi = lista[0][posicao_menor_qi]

    maiores_qis = sorted(lista[1], reverse=True)
    for q1 in maiores_qis:
        print(f'{lista[0][lista[1].index(q1)]}')
    menores_qis = sorted(lista[1], reverse=False)
    for qi in menores_qis:
        print(f'{lista[0][lista[1].index(qi)]}')

except ValueError:
    print('Cuidado com as variáveis')
