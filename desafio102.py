t = 'DESAFIO 102 - FUNÇÃO FATORIAL COM PARAMETRO OPCIONAL'
print(f'{t:=^105}')

def fatorial(a, b = False):
    """
       -> Calcula o fatorial do número digitado.
    :return: Retorna o valor de n.
    :param a: O  número a ser calculado
    :param b: (opcional) mostrar ou não a conta.
    :return: Retorna o valor de a.
    """
    f = 1
    c = 1
    for a in range(a, 0, -1):
        f *= a
        if b == True:
            print(f'{a}', end=' ')
            if a > 1:
                print(f'x', end=' ')
            else:
                print('=', end=' ')
    print(f)

fatorial(3, True)
help(fatorial)