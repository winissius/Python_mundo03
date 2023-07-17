t = 'DESAFIO 90 - DICIONÁRIO, NOME, MÉDIA E SIATUAÇÃO DE ALUNO'
print(f'{t:=^105}')

boletim = {}

nome = str(input('Nome: '))
média = float(input('Média: '))
boletim['nome'] = nome
boletim['média'] = média
if média >= 7:
    boletim['situação'] = 'Aprovado'
else:
    boletim['situação'] = 'Reprovado'

for k, v in boletim.items():
    print(f'{k} é igual a {v}')