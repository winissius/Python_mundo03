v = []
count = 0
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0:
        v.append(n)
        print('Adicionado ao final da lista')
    elif n > v[-1]:
        v.append(n)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(v):
            if n <= v[pos]:
                v.insert(pos, n)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1
print(v)
