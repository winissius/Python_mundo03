def soma(a, b):
    print(f'a = {a} e b = {b} ')
    s = a + b
    print(f'A soma a + b = {s}')


# programa principal
soma(4, 2)
soma(7, 3)
soma(0, 3)

#EMPACOTAR PARAMETROS
print('-'*30)


def contador(*num): #num -> empacota n números
    print(f'Foram passados {len(num)} números e os números são {num}') # -> empacotar gera uma tupla


contador(1, 2, 3, 4, 5)
contador(1, 2)
contador(1, 2, 3)

#TRABALHANDO COM LISTAS
print('-'*30)


def dobralista(lista):
    nlista = []
    for n in lista:
        n *= 2
        nlista.append(n)
    print(nlista)



valores = [7, 2, 5, 0, 4]
dobralista(valores)