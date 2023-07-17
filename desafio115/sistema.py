from desafio115.lib.interface import * # * importa tudo
from desafio115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    n = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if n == 1:
        lerArquivo(arq)
    elif n == 2:
        cabeçalho('Cadastro de pessoas')
        nome = str(input('Nome:'))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif n == 3:
        cabeçalho('Saindo do sistema... Até logo')
        break
    else:
        print('ERRO! Digite uma opção cadastrada')
    sleep(2)