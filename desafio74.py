t = 'DESAFIO 74 - TUPLAS - TABELA ALEATÓRIO E COM SORT'
print(f'{t:=^105}')

from random import randint

n = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)

print(f'Os valores sorteados foram {n}')

#print(f'O maior é {sorted(n)[4]}')
print(f'O maior é {max(n)}')
#print(f'O menor é {sorted(n)[0]}')
print(f'O menor é {min(n)}')