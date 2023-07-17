def lin():
    print('--' * 30)
def mensagem(txt):
    print('--' * 30)
    print(txt)
    print('--' * 30)


#programa princial
lin()
print('AULA 3')
lin()
mensagem('SISTEMA DE ALUNOS')
lin()
lin()


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B é {s}')

#programa principal
soma(4, 5)
soma(8, 9)
soma(2, 1)
soma(a = 5, b = 4)
lin()
lin()
#EMPACOTAR PARAMETROS
def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são {tam} valores')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
lin()
lin()


#UTILIZANDO LISTAS

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *=2
        pos +=1


valores = [6, 3, 9, 1, 0, 2]
print(valores)
dobra(valores)
print(valores)