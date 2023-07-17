t = 'DESAFIO 103 - FUNÇÃO FICHA COM RETORNO E PARAMETROS OPCIONAIS'
print(f'{t:=^105}')

def ficha(jogador, gols = 0):
    print (f'O jogador {jogador} fez {gols} gol(s) no campeonato.')


j = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
#print(ficha(j, g))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if j.strip() == '':
    ficha(jogador='<desconhecido>', gols=g)
else:
    ficha(j, g)