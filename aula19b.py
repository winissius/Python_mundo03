pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas.keys():
    print(k)
for k in pessoas.values():
    print(k)
for k, v in pessoas.items():
    print(f'O {k} = {v}')
print('-='*32)
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil = [] #lista
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])
print('-='*32)
estado = dict()
brasil = list()
for c in range (0, 2):
    estado['uf'] = str(input('Estado: '))
    estado['sigla'] = str(input('Sigla '))
    brasil.append(estado.copy())
for e in brasil:
    '''for k, v in e.items():
        print(f'{k} = {v}')'''
    for v in e.values():
        print(f'{v}', end=' ')

