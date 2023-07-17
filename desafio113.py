t = 'DESAFIO 113 - TRATAMENTO DE ERRO, FUNÇÃO LEIAINT E LEIAFLOAT'
print(f'{t:=^105}')

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


def leiaFloat(n):
    while True:
        try:
            n = float(input(n))
        except (TypeError, ValueError):
            print(f'ERRO! Digite um número inteiro válido ')
            continue
        except KeyboardInterrupt:
            print(f'ERRO! O usuário preferiu não digitar')
            return 0
        else:
            return n
            break


#PROGRAMA PRINCIPAL
i = leiaInt('Digite um inteiro: ')
r = leiaFloat('Digite um real: ')
print(f'O valor inteiro digitado foi {i} e o real foi {r}')