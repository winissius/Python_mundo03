t = 'DESAFIO 72 - TUPLAS - CONTAGEM POR EXTENSO'
print(f'{t:=^105}')

b = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco')
n = 1
while True:
    n = int(input('Digite o número que deseja ver por extenso [0 a 5]:  '))
    if 5 >= n >= 0:
        break
    print('Tente novamente.', end=' ')

print(f'Você digitou {n} e seu número por extenso é: {b[n]}')
