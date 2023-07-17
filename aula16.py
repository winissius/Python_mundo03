lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
'''print(lanche[1])
print(lanche[1:3])
print(lanche[-1])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2:])'''

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi para caramba!')

for cont in range (0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
print('Comi para caramba!')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi para caramba!')

print(sorted(lanche)) #coloca em ordem alfabética

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
d = b +a
print(c)
print(d)

print(f'o número 5 se repete {c.count(5)} vezes') #conta quantas vezes tem o 5
print(f'{d.index(2 )}') #retorna a posição
print(f'{d.index(5, 1 )}') #retorna a posição com deslocamento de 1 casa

pessoa = ('Gustavo', 39, 99.88)
#del(pessoa) #apaga da memoria
print(pessoa)