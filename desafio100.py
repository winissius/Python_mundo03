t = 'DESAFIO 100 - FUNÇÃO SORTEADORA E SOMADORA DE PARTES'
print(f'{t:=^105}')

from random import randint
from time import sleep

numeros = []


def sortear():
    print('Sorteando 5 valores', end=' ')
    for n in range(0, 5):
        valor = (randint(0, 10))
        print(f'{valor}', end=' ')
        sleep(0.5)
        numeros.append(valor)
    print('PRONTO!')


def somaPar(lst):
    par = 0
    print(f'\nSomando os valores de {numeros}, temos', end=' ')
    for valores in numeros:
        if valores % 2 == 0:
            par += valores
    print(f'{par}')


sortear()
somaPar(numeros)