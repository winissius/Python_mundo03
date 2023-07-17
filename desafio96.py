t ='DESAFIO 96 - ÁREA DE TERRO COM FUNÇÕES'
print(f'{t:=^105}')

def area(a, b):
    print(f'A área de um terrneno {a}m x {b}m é de {a*b}m²')
print('Controle de terrenos')
print('-'*20)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)