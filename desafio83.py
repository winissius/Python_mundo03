t = 'DESAFIO 83 - VERIFICADOR DE EXPRESSÕES MATEMÁTICAS COM PARÊNTESES E LISTAS'
print(f'{t:=^105}')

e = str(input(('Digite uma expressão matemática com parênteses\n')))
lista = []

for l in e: # cria uma variável 'l' e verifica em cada parte da lista(string)
    if l == '(':
        lista.append('(')
    elif l == ')':
        if len(lista) > 0:
            if l == ')':
                lista.pop()
        else:
            lista.append(')')
            #break

if len(lista) == 0:
    print('Expressão verdadeira')
else:
    print('Expressão falsa')