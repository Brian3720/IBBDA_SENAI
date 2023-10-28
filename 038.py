'''
Crie uma calculadora que após ler 3 valores, mostre e opere de acordo com as opções:

1.	Somar
2.	Multiplicar
3.	Maior
4.	Novos números
5.	Sair do programa
'''


valor1 = int(input('digite um número: '))
valor2 = int(input('digite um número: '))
valor3 = int(input('digite um número: '))
opcao = 0

while opcao != 5:
    opcao = input('Qual operação deseja fazer?'
                  '\n O que você deseja fazer:'
                    '\n 1 - Somar'
                    '\n 2 - Multiplicar'
                    '\n 3 - Maior número dentre os 3'
                    '\n 4 - Inserir 3 novos números'
                    '\n 5 - Sai do programa')

    if opcao == 1:
       soma = valor1 + valor3 + valor3
       print(f'A soma dos 3 valores é {soma}')
       resposta = input('Deseja fazer outra operação, basta digitar "Continuar"').strip().lower()
    elif opcao == 2:
        mult = valor1 * valor2 * valor3
        print(f'A multiplicação dos 3 valores é {mult}')
    elif opcao == 3:
        if valor1 > valor2 and valor1 > valor3:
            print(f'O número maior dentre {valor1, valor2, valor3} é {valor1}')
        elif valor2 > valor1 and valor2 > valor3:
            print(f'O número maior dentre {valor1, valor2, valor3} é {valor2}')
        else:
            print(f'O número maior dentre {valor1, valor2, valor3} é {valor3}')
    elif opcao == 3:
        print('Escolha 3 novos valores')
        valor1 = int(input('digite um número: '))
        valor2 = int(input('digite um número: '))
        valor3 = int(input('digite um número: '))


