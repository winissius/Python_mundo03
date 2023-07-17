'''pessoas = {'nomes': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nomes"]} tem {pessoas["idade"]}')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

#del pessoas['sexo']
pessoas['nomes'] = 'Leandro'

pessoas['peso'] = 98.5

for k in pessoas.keys():
    print(k)

for v in pessoas.values():
    print(v)

for k, v in pessoas.items():
    print(f'{k} = {v}')'''

'''estado1 = {'uf': 'Rio de Janeiro', 'siga': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}i
brasil = []
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['uf'])'''
estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input("Unidade Federativa: "))
    estado['sigla'] = str(input("Unidade Federativa: "))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        #print(f'o campo {k} tem valor {v}')
        print(v)
