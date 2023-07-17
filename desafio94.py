t = 'DEASFIO 94 UNINDO DICIONARIOS E LISTAS PARA CADASTRAR E ANALISAR PESSOAS'
print(f'{t:=^105}')
pessoas = {}
galera = []
soma = 0
while True:
    continuar = sexo = 'k'
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO! Por favor digite apenas M ou F')
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    while True:
        continuar = str(input('Quer continuar [S/N]')).upper().strip()[0]
        if continuar in 'SN':
            break
        print('Erro! Por favor digite apenas S ou N')
    galera.append(pessoas.copy())
    if continuar == 'N':
        break
print('-='*30)
print(galera)
print(f'A) Foram cadastradas {len(galera)} pessoas')
med = soma/len(galera)
print(f'B) A média das idades é {med:5.2f} anos')
print(f'C) As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(p['nome'], end=' ')
print()
print(f'D) As pessoas com a idade acima da média são: ')
for p in galera:
    if p['idade'] >= med:
        #print(p['nome'], end =' ')
        for k, v in p.items():
            print(f'{k} = {v}', end=' ')
        print()
print('<<ENCERRADO>>')


