'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta
#### REVISAR ####
'''

def verifica_parenteses(expressao):
    pilha = []
    for caractere in expressao:
        if caractere == '(':
            pilha.append('(')
        elif caractere == ')':
            if not pilha:
                return False  # Parêntese fechado sem um correspondente aberto
            pilha.pop()

    return not pilha  # A expressão está correta se a pilha estiver vazia no final

# Solicitar a expressão ao usuário
expressao = input("Digite uma expressão com parênteses: ")

# Verificar se os parênteses estão corretos
if verifica_parenteses(expressao):
    print("Os parênteses estão corretos na expressão.")
else:
    print("Os parênteses não estão na ordem correta na expressão.")

