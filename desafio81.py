t = 'DESAFIO 81 - ANALISADOR DE LISTAS'
print(f'{t:=^105}')

lista = []

while True:
    r = 'k'
    n = int(input('Digite um valor: '))
    lista.append(n)
    while r not in 'SsNn':
        r = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if r == 'N':
        break
print(f'Você digitou {len(lista)} valores')
lista.sort(reverse=True)
print(f'Os valores da sua lista em ordem decrescente são: {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
print('feshow!')