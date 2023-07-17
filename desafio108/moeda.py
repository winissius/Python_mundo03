def aumentar(preço=0, taxa=0):
    return preço * (1 + taxa / 100)



def diminuir(preço=0, taxa=0):
    return preço * (1 - taxa/100)


def dobro(preço=0):
    return preço * 2


def metade(preço=0):
    return preço / 2

def moeda(preço=0, moeda='R$'):
    p = preço
    return (f'{moeda} {p:>8.2f}').replace('.',',')
