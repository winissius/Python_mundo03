def linha(a=42):
    print("-"*a)


def cabeçalho(msg):
    linha()
    print(msg.center(42).upper())
    linha()


def menu(lista):
    cabeçalho('Menu principal')
    count = 1
    for i in lista:
        print(count, end='   ')
        print(i)
        count += 1
    linha()
    n = leiaInt('Sua opção: ')
    return int(n)



def leiaInt(n):
    while True:
        try:
            n = int(input(n))
        except (TypeError, ValueError):
            print(f'ERRO! Digite um número inteiro válido ')
            continue
        except KeyboardInterrupt:
            print(f'ERRO! O usuário preferiu não digitar')
            return 0
        else:
            return n
            break

def leiaNome(n):
    while True:
        n = str(input('Nome: '))
        if n.isalpha():
            return (n)
            break
        else:
            print('Digite um nome composto apenas por letras')