t = 'DESAFIO 89 LISTA DENTRO DE LSITAS, BOLETIM COM ALUNO DISCRETIZAVEL'
print(f'{t:=^105}')
sala = []
aluno = []
while True:
    while True:
        r = 'k'
        a = '1'
        nome = str(input('Nome:')).title()
        nota1 = float(input('Nota 1: '))
        nota2 = float(input('Nota 2: '))
        med = (nota1+nota2)/2
        aluno.append(nome)
        aluno.append(nota1)
        aluno.append(nota2)
        aluno.append(med)
        while r not in 'SN':
            r = str(input('Quer conitnuar [S/N]')).upper().strip()[0]
        sala.append(aluno[:])
        aluno.clear()
        if r == 'N':
            break
    print('-=' * 20)
    print('No   NOME           MÉDIA')
    print('-' * 25)
    for i, al in enumerate(sala):
        print(f'{i:<5}{al[0]:<16}{al[3]:>3}')
    print('-' * 25)
    while a != 999:
        a = int(input('Digite o código do aluno que deseja ver [999 para finalziar]:'))
        if a != 999 and a <= len(sala)-1:
            print(f'Notas de {sala[a][0]} são: [{sala[a][1]}, {sala[a][2]}]')
    if a == 999:
        break
print('feshow!')