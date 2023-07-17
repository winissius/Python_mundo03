t = 'DESAFIO 75 - TUPLAS - CRIADA COM WHILE E UTILIZADNO INDEX'
print(f'{t:=^105}')

count = a = b = c = d = e = 0
t = (a, b, c, d, e)
'''while count !=5:
    n = int(input('Digite seu número: '))
    count += 1
    if count == 1:
        a = n
    else:
        if count == 2:
            b = n
        elif count == 3:
            c = n
        elif count == 4:
            d = n
        else:
            e = n
    t = (a, b, c, d, e)'''
t = ((int(input('Digite um número '))),
     (int(input('Digite um número '))),
     (int(input('Digite um número '))),
     (int(input('Digite um número '))),
     (int(input('Digite um número '))))
print(f'Você digitou os valores: {t}')
print(f'O número 9 apareceu {t.count(9)} vezes')
if t.count(3) == 0:
    print('O número 3 não foi digitado nenhuma vez')
else:
# if 3 in t:
    print(f'O número 3 aparece na {t.index(3)} posição')
print(f'os números pares digitados foram:', end=' ')
for k in t:
    if k % 2 == 0:
        print(k, end=' ')
'''print(f'{t[0]}' if t[0] % 2 == 0 else '', end=' ')
print(f'{t[1]}' if t[1] % 2 == 0 else '', end=' ')
print(f'{t[2]}' if t[2] % 2 == 0 else '', end=' ')
print(f'{t[3]}' if t[3] % 2 == 0 else '', end=' ')
print(f'{t[4]}' if t[4] % 2 == 0 else '', end=' ')'''
