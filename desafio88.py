print('-'*20)
print('{:^20}'.format('JOGO DA MEGA SENA'))
print('-'*20)

from random import randint
from time import sleep
lista = []
jogos = []
count = 0
n = int(input('Quantos jogos?'))
while True:
    for c in range(1, 7):
        while len(jogos) < 6:
            v = randint(1, 60)
            if v not in jogos:
                jogos.append(v)
    if jogos not in lista:
        lista.append(jogos[:])
    jogos.clear()
    count += 1
    if n == count:
        break
for i in range(0, len(lista)):
    lista[i].sort()
    print(f'Jogo {i+1}:{lista[i]}')
    #sleep(.5)
print('Fim de jogo, boa sorte!')

