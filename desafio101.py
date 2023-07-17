t = 'DESAFIO 101 - FUNÇÃO COM RETORNO E VALORES OPCIONAIS'
print(f'{t:=^105}')

def voto(a):
    from datetime import date
    atual = date.today().year
    idade = int(atual - ano)
    print(f'Com {idade} anos:', end=' ')
    if 65 >= idade >= 18:
        return ('VOTO OBRIGATÓRIO')
    elif idade < 16:
        return ('NÃO VOTA')
    else:
        return ('VOTO OPCIONAL')

ano = int(input('Em que ano você nasceu? '))
print(voto(ano))