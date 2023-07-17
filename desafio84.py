t = 'LISTA DENTRO DE LSITAS, ANALISE DE PESSOAS E PESOS'
print(f'{t:=^105}')

pessoas = []
dados = []
maior = menor = count= 0
nmaior = []
nmenor = []
while True:
    r = 'k'
    dados.append(str(input('Nome: ').title()))
    dados.append(int(input('Peso [kg]: ')))
    pessoas.append(dados[:])
    dados.clear()
    #count += 1
    while r not in 'SsNn':
        r = str(input('Deseja continuar [S/N] ')).upper().strip()[0]
    if r == 'N':
        break
print(f'Foram cadastradas {len(pessoas)} pessoas')
for c in range(0, len(pessoas)):
    if c == 0:
        maior = menor= pessoas[c][1]
        nmaior = nmenor = pessoas[c][0]
    else:
        if pessoas[c][1] > maior:
            maior = pessoas[c][1]
        elif pessoas[c][1] < menor:
            menor = pessoas[c][1]
print(f'O maior peso foi {maior}. Peso de', end=' ')
for n in pessoas:
    if n[1] == maior:
        print(f'[{n[0]}]', end=' ')
print(f'\nO menor peso foi {menor}. Peso de', end=' ')
for n in pessoas:
    if n[1] == menor:
        print(f'[{n[0]}]', end=' ')
