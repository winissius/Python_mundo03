t = 'AULA 15 - while True break'
print('{:=^105}'.format(t))

c = 1
s = 0

'''while c <= 10:
    print(c, '-> ',end ='')
    c += 1
print('FESHOW')'''

while True:
    n = int(input('digite um número: '))
    if n == 999:
        break
    s += n
print('A soma é {}'.format(s))
print(f'A soma é {s}')

nome = 'Dedessa'
idade = 23

print(f'A {nome} tem {idade} anos')