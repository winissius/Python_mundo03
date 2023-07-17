'''t = 'LISTAS(parte1)'
print(f'{t:=^105}')

num = [2, 5, 9, 1]
print(num)
num.append(7)
print(num)
print(f'Essa lita tem {len(num)} elementos')
num.sort(reverse=True) # de trás para frente
print(num)
num.pop() # remove o ultimo
num.pop(2) # remove o indice 2
print(num)
num.insert(0,7)
print(num)
num.remove(7) # remove o primeiro da esquerda para direita
print(num)
if 4 in num:
    num.remove(4) # remove se encontrar
else:
    print('não achei o número 4')
print(num)'''
'''#lista mais bonitinha
valores = [] #ou list()
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)
'''
valores = [1,2,3,4]
'''for c in range(0,5):
    valores.append(int(input('Digite um valor')))'''

for c,v in enumerate(valores):
    print(f'na posição {c} encontrei o valor {v}!')
print('cheguei ao final da lista')

'''a = [2, 3, 4, 7]
b = a # a partir de igular o py cria uma ligação entre listas
b = a[:] # uma cópia
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')'''

