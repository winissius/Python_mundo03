t = 'DESAFIO 91 - DICIONÁRIO, RANKING DE 4 JOGADORES JOGANDO DADOS D6'
print(f'{t:=^105}')

from random import randint
from time import sleep
from operator import itemgetter
maior = ''
print('Valores sorteados:')
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.5)

'''if jogo['jogador1']>jogo['jogador2'] and jogo['jogador1'] > jogo['jogador3'] and jogo['jogador1'] > jogo['jogador4']:
    maior = jogo['jogador1']
elif jogo['jogador2'] > jogo['jogador1'] and jogo['jogador2'] > jogo['jogador3'] and jogo['jogador2'] > jogo['jogador4']:
    maior = jogo['jogador2']
elif jogo['jogador3'] > jogo['jogador1'] and jogo['jogador3'] > jogo['jogador2'] and jogo['jogador3'] > jogo['jogador4']:
    maior = jogo['jogador3']
else:
    maior = jogo['jogador4']'''
ranking = list()
print('=-'*50)
print(f'{"== Ranking dos jogadores ==": ^100}')

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}o lugar: {v[0]} com {v[1]}')
    sleep(0.5)
