t = 'DESAFIO 97 - TÍTULO ADAPTAVEL COM FUNÇÕES'
print(f'{t:=^105}')

def mensagem(txt):
    print('~'*(len(txt)+2))
    print(f' {txt}')
    print('~'*(len(txt)+2))
txt1 = 'Gustavo Guanabara'
txt2 = 'Cusso de Python no Youtube'
txt3 = 'CeV'

mensagem(txt1)
mensagem(txt2)
mensagem(txt3)