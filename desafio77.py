t = 'DESAFIO 77 - CONTADOR DE VOGAIS COM TUPLA'
print(f'{t:=^105}')

palavras = ('aprender', 'programar','linguagem', 'python'
            'curso', 'gratis', 'estudar', 'praticar',
            'tabalhar', 'mercado', 'programador', 'futuro')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos:', end=' ')
    for l in p:
        if l in 'aeiou':
            print(l, end=' ')

'''for p in palavras:
    print(f'\nNa palavra {p.upper()} temos', end=' ')
    for l in p:
        if l.lower() in 'aeiou':
            print(l, end=' ')'''