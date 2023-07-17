t = 'DESAFIO 73 - TUPLAS - TABELA DO BRASILEIRÃO'
print(f'{t:=^105}')

times = ('Corinthias', 'Atlético-MG', 'SP', 'Santos', 'Coritiba', 'Avaí', 'América-MG', 'Pameiras', 'Bragantino', 'Botafogo')

print(f'Os 5 primeiros são: {times[:5]}')
print(f'Os 4 últimos são {times[-4:]}')
print(f'Times em ordem alfabética: \n{sorted(times)}')
print(f'O Coxa está em {times.index("Coritiba")+1}a posição')
