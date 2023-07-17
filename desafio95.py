t = 'DESAFIO 95 - JOGADOR DE FUTEBOL COM DICIONÁRIOS - APRIMORADO'
print(f'{t:=^105}')
from time import sleep
aproveitamento = {}
ngols = []
jogador = {}
time = []
total = 0
while True:
    jogador.clear()
    nome = str(input('Nome do jogador:')).title()
    jogador['nome'] = nome
    partidas = int(input(f'Quantas partidas {nome} jogou?'))
    for c in range(1, partidas + 1):
        gols = int(input(f'Quantos gols na partida {c}:'))
        ngols.append(gols)
        total += gols
    jogador['partidas'] = partidas
    jogador['gols'] = ngols[:]
    jogador['total'] = total
    time.append(jogador.copy())
    total = gols = 0
    ngols.clear()
    while True:
        r = str(input('Quer continuar?[S/N]')).upper().strip()[0]
        if r in 'SsNn':
            break
        print('ERRO! Digite S ou N!')
    if r == 'N':
        break
print('=-'*28)
print(f'{"COD":<8}{"JOGADOR":<18}{"GOLS":<20}{"TOTAL":<10}')
for l in range(0, len(time)):
    print(f'{l:<8}{time[l]["nome"]:<18}{str(time[l]["gols"]):<20}{time[l]["total"]:<10}')
print('=-'*28)
while True:
    j = int(input('Qual jogador deseja ver mais dados? [999 para parar]'))
    if j == 999:
        break
    if j >= len(time):
        print(f'ERRO! Não existe jogador com o código {j}')
    else:
        print(f'Levantamento do jogador {time[j]["nome"]}')
        for k in range (0,time[j]['partidas']):
            print(f'No jogo {k+1} fez {time[j]["gols"][k]} gols')
            sleep(0.5)
print("feshow")