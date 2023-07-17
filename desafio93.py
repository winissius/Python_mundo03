t = 'DESAFIO 93 - JOGADOR DE FUTEBOL COM DICIONÁRIOS'
print(f'{t:=^105}')
aproveitamento = {}
ngols = []
total = 0
nome = str(input('Nome do jogador:'))
aproveitamento['nome'] = nome
partidas = int(input(f'Quantas partidas {nome} jogou?'))
for c in range(1, partidas + 1):
    gols = int(input(f'Quantos gols na partida {c}:'))
    ngols.append(gols)
    total += gols
aproveitamento['gols'] = ngols
aproveitamento['total'] = total
print('=-'*35)
print(aproveitamento)
print('=-'*35)
for k, v in aproveitamento.items():
    print(f'O campo {k} tem o valor {v}')
print('=-'*35)
print(f'O jogador {aproveitamento["nome"]} jogou {partidas} partidas')
for f,l in enumerate(aproveitamento['gols']):
    print(f'=> Na partida {f+1}, fez {l} gols')
print(f'Foi um total de {aproveitamento["total"]} gols.')
