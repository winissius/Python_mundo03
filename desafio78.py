t = 'DESAFIO 78 - MAIOR E MENOR VALORES NA LISTA'
print(f'{t:=^105}')

n = []
maior = 0
menor = 0
for c in range(0, 5):
    n.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = n[c]
    else:
        if n[c] > maior:
            maior = n[c]
        if n[c] < menor:
            menor = n[c]
print(f'Você criou a lista: {n}')
print(f'O maior valor da lista é {maior} e pode ser encontrado nas posições: ', end='')
for i, v in enumerate(n):
    if v == maior:
        print(f'{i}...', end='')
print(f'\nO menor valor da lista é {menor} e pode ser encontrado nas posições: ', end='')
for i, v in enumerate(n):
    if v == menor:
        print(f'{i}...',end='')