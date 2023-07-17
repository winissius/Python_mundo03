t = 'DESAFIO 80 - INSERIR NUMEROS ORDENADOS SEM UTILZIAR O COMANDO SORT'
print(f'{t:=^105}')

valores = []
c = 0
for v in range(0, 5):
    n = int(input('Digite um valor '))
    if v == 0:
        valores.append(n)
    elif n > valores[-1]:
        valores.append(n)
    #if c == 0 or n > valor[-1]: elimina o elif
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                break
            pos += 1
print(valores)

