def leiaDinheiro(msg):
    #valido = False
    while True:
        n = str(input(msg)).strip().replace(',', '.')
        if n.isalpha() or n == '':
            print(f'ERRO: {n} é um preço inválido')
        else:
            return float(n)
            break