t = 'DESAFIO 87 LISTA DENTRO DE LSITAS, MATRIZ 3X3'
print(f'{t:=^105}')
matriz = [[], [], []]
for c in range(0, 3):
    n = int(input(f'Digite um valor para a {0, c}'))
    matriz[0].append(n)
for c in range(0, 3):
    n = int(input(f'Digite um valor para a {1, c}'))
    matriz[1].append(n)
for c in range(0, 3):
    n = int(input(f'Digite um valor para a {2, c}'))
    matriz[2].append(n)
print('-='*20)
for c in range(0,3):
    print(f'[ {matriz[0][c]:^5} ]', end =' ')
print()
for c in range(0, 3):
    print(f'[ {matriz[1][c]:^5} ]', end =' ')
print()
for c in range(0, 3):
    print(f'[ {matriz[2][c]:^5} ]', end =' ')
print()
print('-='*20)
soma1 = soma2 = soma3 = 0
for c in range(0,3):
    if matriz[0][c] % 2 == 0:
        soma1 += matriz[0][c]
    if matriz[1][c] % 2 == 0:
        soma2 += matriz[1][c]
    if matriz[2][c] % 2 ==0:
        soma3 += matriz[2][c]
print(f'A soma dos pares é {soma1 + soma2 + soma3}')
print(f'A soma dos valores da terceira coluna é {matriz[0][2]+matriz[1][2]+matriz[2][2]}')
soma = count = 0
for v in matriz:
    maior = matriz[1][0]
    if matriz[1][1] > matriz[1][0] and matriz[1][1] > matriz[1][2]:
        maior = matriz[1][1]
    elif matriz[1][2] > matriz[1][0] and matriz[1][2] > matriz[1][1]:
        maior = matriz[1][2]
print(f'O maior número da segunda linha é {maior}')
