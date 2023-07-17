t = 'DESAFIO 79 - VALORES ÚNICOS NA LISTA'
print(f'{t:=^105}')

valores=[]
c = 0
while True:
    valores.append(int(input('Digite um valor: ')))
    if valores.count(valores[c]) > 1:
        print('Valos duplicado! Não vou adicionar')
        valores.pop()
    else:
        print('Valor adicionado com sucesso')
        c += 1
    continuar = 's'
    while continuar not in 'NS':
        continuar = str(input('Deseja continuar [S/N]')).upper().strip()[0]
    if continuar == 'N':
        break
valores.sort()
print(valores)
print('Feshow')

