'''
Crie uma tupla preenchida com os 10 filmes mais assistidos de todos os tempos, e depois mostre:

Apenas os 3 primeiros mais assistidos
Os últimos 2 mais assistidos
A lista em ordem alfabética
Em que posição está “O rei leão”
'''
#______________ Os 10 filmes mais assistidos de todos os tempos _________________
#   1   Avatar
#   2   Titanic
#   3   Star Wars: O Despertar da Força
#   4   Jurassic World
#   5   Os Vingadores
#   6   Velozes & Furiosos 7
#   7   Os Vingadores: Era de Ultron
#   8   Harry Potter e as Relíquias da Morte Parte 2
#   9   O Rei Leão
#   10  Vingadores: Ultimato



filmes_mais_assistidos = ('Avatar', 'Titanic', 'Star Wars: O Despertar da Força', 'Jurassic World', 'Os Vingadores',
                          'Velozes & Furiosos 7', 'Os Vingadores: Era de Ultron', 'Harry Potter e as Relíquias da Morte Parte 2',
                          'O Rei Leão', 'Vingadores: Ultimato')


print(f'\n\n\n'
      f'Exercicio de número 054'
      f'\n__________________________________'
      f'\nOs 3 primeiros mais assistidos foram:'
      f'\n__________________________________'
      f'\n{filmes_mais_assistidos[:3]}'
      f'\n__________________________________'
      f'\nOs 2 últimos mais assistidos foram:\n'
      f'\n__________________________________'
      f'\n{filmes_mais_assistidos[8:10]}'
      f'\n__________________________________\n'
      f'\nLista em ordem alfabética {sorted(filmes_mais_assistidos)}'
      f'\n'
      f'\n O filme Rei Leão está na posição {filmes_mais_assistidos.index('O Rei Leão') + 1}º')
