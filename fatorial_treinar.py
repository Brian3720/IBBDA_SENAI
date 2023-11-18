numero = int(input('Digite um número: '))

fatorial = 1

while numero > 0:
    fatorial *= numero
    numero  -= 1

print(f'O fatorial de {numero} é {fatorial}')