t = 'DESAFIO 99 - FUNÇÃO CLASSIFICADORA'
print(f'{t:=^105}')

from time import sleep

def maior(* num):
    nmaior = contador = 0
    sleep(0.5)
    print('Analisando os valors passados...')
    for valor in num:
        if valor >= nmaior:
            nmaior = valor
        print(f'{valor}', end=' ')
        contador += 1
    '''print("-="*20)'''
    print(f'foram informanados {contador} valores')
    print(f'O mairo valor foi {nmaior}')
    print("-="*20)


#Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()