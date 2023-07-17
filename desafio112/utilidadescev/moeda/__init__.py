def aumentar(preço=0, taxa=0, formato=False):
    res = preço * (1 + taxa / 100)
    return res if formato is False else moeda(res)



def diminuir(preço=0, taxa=0, formato=False):
    res = preço * (1 - taxa/100)
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if formato is False else moeda(res)


def metade(preço=0, formato=False):
    res = preço / 2
    return res if formato is False else moeda(res)


def moeda(preço=0, moeda='R$', format=False):
    return (f'{moeda} {preço:.2f}').replace('.',',')


def resumo(preço=0,aumento=0,redução=0):
    print('-'*36)
    print(f'RESUMODO VALOR'.center(36))
    print('-' * 36)
    print(f'Preço analisado:     \t{moeda(preço)}')
    print(f'Dobro do preço:     \t{moeda(dobro(preço))}')
    print(f'Metade do preço:     \t{metade(preço, True)}') #outra forma
    print(f'{aumento}% de aumento:      \t{aumentar(preço, aumento, True)}')
    print(f'{redução}% de redução:      \t{diminuir(preço, redução, True)}')
    print('-' * 36)