t = 'DESAFIO 82 - LISTA, LISTA DE PARES E LSITA DE IMPARES'
print(f'{t:=^105}')

l = []
li = []
lp = []
while True:
    r = 'k'
    n = int(input('Digite um valor: '))
    l.append(n)
    if n % 2 == 0:
        lp.append(n)
    elif n % 2 != 0:
        li.append(n)
    while r not in 'SsNn':
        r = str(input('Continuar [S/N]')).upper().strip()[0]
    if r == 'N':
        break
print(f'A lista compelta é {l}')
print(f'A lista dos impares é {li}')
print(f'A lista dos pares é {lp}')
print('feshow!')
par = []
impar = []
#outra solução
for pos, valor in enumerate(l):
    if valor % 2 == 0:
        par.append(valor)
    elif valor % 2 != 0:
        impar.append(valor)
print(par)
print(impar)