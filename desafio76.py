t = 'DESAFIO 76 - LISTAGEM DE PREÇO COM TUPLA MISTA'
print(f'{t:=^105}')

print('-'*33)
print('{:^33}'.format('LISTAGEM DE PREÇOS'))
print('-'*33)
0
n = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.9, 'Estojo', 25)

for k in range (0,len(n),2):
    print(f'{n[k]:.<23} R$', end='')
    '''for j in range (1, len(n), 2):
        print(n[j])'''
    if k % 2 == 0:
        print(f'{n[(k+1)]:>7.2f}')
print('-'*33)

