t = 'DESAFIO 92 - CADASTRO DE TRABALHADOR EM DICIONARIO'
print(f'{t:=^105}')

from datetime import date


trabalhador = {}
atual = date.today().year
CTPS = 1


while True:
    '''trabalhador = {'nome': str(input('Nome: ')),
                   'idade': (atual - int(input('Ano de nascimento: '))),
                   'CTPS:': int(input('Carteira de trabalho: '))}'''
    trabalhador['nome'] = str(input('Nome: '))
    trabalhador['idade'] = (atual - int(input('Ano de nascimento: ')))
    trabalhador['CTPS'] = int(input('Carteira de trabalho: [0 não tem] '))
    if trabalhador['CTPS'] == 0:
        break
    trabalhador['contratação'] = int(input('Ano de contratação: '))
    trabalhador['salário'] = float(input('Salário: R$'))
    trabalhador['aposentadoria'] = ((trabalhador['contratação'] + 35)-(atual-trabalhador['idade']))
    if trabalhador['salário'] != 0:
        break
print('-='*30)
for k, v in trabalhador.items():
    print(f'{k} tem o valor de {v}')