v = []
count = 0
maior = menor = 0
for c in range(0,5):
    n = int(input(f'Digite um valor para a posição {count}: '))
    v.append(n)
    if c == 0:
        maior = menor = v[0]
    else:
        if v[c] > maior:
            maior = v[c]
        elif v[c] < menor:
            menor = v[c]
    count += 1
print(f'Sua lista é {v}')
for p, val in enumerate(v):
    if val == maior:
        print(f'O maior valor é {maior} na posição {p}')
    elif val == menor:
        print(f'O menor valor é {val} na posição {p}')