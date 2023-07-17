t = 'DESAFIO 106 - FUNÇÃO INTERACTIVE HELP'
print(f'{t:=^105}')

def interactiveHelp(k):
    while True:
        r = str(input(k)).strip().lower()[:3]
        if r == 'fim':
            break
        help(r)
    print('Volte logo!')

interactiveHelp('Função ou biblioteca:')