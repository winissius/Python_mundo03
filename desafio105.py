t = 'DESAFIO 105- FUNÇÃO COM ENTRADA DE INFINITAS NOTAS E SITUAÇÃO OPCIONAL'
print(f'{t:=^105}')

def notas(*n, sit = False):
    """
    -> FUNÇÃO QUE RECEBE A ENTRADA DE VÁRIAS NOTAS
    :param n: ACEITA N NOTAS DE ALUNOS
    :param sit: ESTADO EM RELAÇÃO A MÉDIA
    :return:DICIONÁRIO COM VARIAS NOTAS E SITUAÇÃO (OPCINIAL)
    """
    soma = maior = menor = 0
    count = len(n)
    for p, v in enumerate(n):
        if p == 0:
            maior = menor = v
        if v <= menor:
            menor = v
        if v >= maior:
            maior = v
        soma += v
        med = soma/count
        if med >= 9:
            situação = 'ÓTIMA'
        elif med >= 7:
            situação = 'BOA'
        elif med >= 6:
            situação = 'MÉDIA'
        else:
            situação = 'RUIM'
    sala = {'total': count, 'maior': maior, 'menor': menor, 'media': med, 'situação': situação}
    if sit == False:
        del sala['situação']
    return sala



#PROGRAMA PRINCIPAL
resp = notas(10, 9, 10, 9, 10, sit = True)
print(resp)
help(notas)