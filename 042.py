'''
Simulação de um Caixa Eletrônico Este programa simula um caixa eletrônico, permitindo que o usuário faça depósitos,
saques e consulte o saldo da conta, e sair
'''

print('Bem vindo ao caixa eletronico, o que deseja?')

saldo_Atual = 0
opcao = 0

while opcao != 4:
    opcao = input('O que deseja fazer? '
                  '\n1 - Depósito'
                  '\n2 - Saque'
                  '\n3 - Consultar Saldo'
                  '\n4 - Sair')

    if opcao == 1:
        valor_deposito = int(input('O valor do depósito é de: R$ '))
        saldo_Atual = saldo_Atual + valor_deposito
        print(f'Seu saldo atual é de {saldo_Atual}')

        opcao = input('O que deseja fazer? '
                      '\n1 - Depósito'
                      '\n2 - Saque'
                      '\n3 - Consultar Saldo'
                      '\n4 - Sair')
    elif opcao == 2:
        saque = float(input('Valor que deseja retirar: R$ '))

        if saque > saldo_Atual:
            saldo_Atual = saldo_Atual - saque
        else:
            print('Você não tem essa grana!!')

        print(f'Seu saldo atual é de {saldo_Atual}')

    elif opcao == 3:
        print(f'Seu saldo é de R${saldo_Atual}')
    else:
        print('Até a próxima')