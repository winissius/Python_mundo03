v = []
count = 0
while True:
    r = 'k'
    n = int(input('Digite um valor: '))
    if count == 0:
        v.append(n)
        count += 1
    else:
        if n in v:
            print('Valor duplicado, não vou adicionar não')
        else:
            v.append(n)
    while r not in 'SsNn':
        r = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if r == 'N':
        break
print(v)
print('feshow')