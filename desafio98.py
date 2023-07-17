t = 'DESAFIO 98 - FUNÇÃO CONTADOR'
print(f'{t:=^105}')

from time import sleep

def contador(inicio, fim,  passo):
    c = inicio
    print("-=" * 20)
    print(f'CONTAGEM DE {inicio} ATÉ {fim} DE {passo} EM {passo}')
    if inicio > fim:
        while c >= fim:
            print(f'{c}', end=' ')
            c += passo
            sleep(0.2)
        print('FIM!')
    if fim > inicio:
        while c <= fim:
            print(f'{c}', end=' ')
            c += passo
            sleep(0.2)
        print('FIM!')

contador(1, 10, 1)
contador(10, 0, -2)
print('-='*20)
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))