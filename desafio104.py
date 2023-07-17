t = 'DESAFIO 104 - FUNÇÃO ENTRADA DE NÚMERO COM VALIDAÇÃO'
print(f'{t:=^105}')

def leiaInt(k):
    while True:
        n = str(input((k)))
        if n.isnumeric():
            break
        else:
            print('ERRO! Digite um número inteiro válido.')
    return n

#PROGRAMA PRINCIPAL
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')