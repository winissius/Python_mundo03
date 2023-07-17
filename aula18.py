teste = list()
teste.append('Gutavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera)

galera2 = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria',45]]
print(galera2[0][1])

for p in galera2:
    print(f'{p[0]} tem {p[1]} anos de idade')

galera3 = list()
dados = list()

for c in range(0,3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera3.append(dados[:])
    dados.clear()
print(galera3)
totmai = totmen = 0
for p in galera3:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'são {totmai} maiores de idade e {totmen} menores de idade')

sala = []
nome = str(input('Nome:'))
nota1 = float(input('Nota 1'))
nota2 = float(input('Nota 2'))
med = (nota1+nota2) / 2
sala.append([[nome], [[nota1],[nota2]], [med]])
print(sala)