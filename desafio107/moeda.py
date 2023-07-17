def aumentar(preço, taxa):
    return preço * (1 + taxa / 100)



def diminuir(preço, taxa):
    return preço * (1 - taxa/100)


def dobro(preço):
    return preço * 2


def metade(preço):
    return preço / 2

'''def moeda(preço):
    p = preço
    return (f'{p:.2f}')'''
