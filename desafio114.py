t = 'DESAFIO 114 - TRATAMENTO DE ERRO, VERIFICADOR DE SITE ONLINE'
print(f'{t:=^105}')

import urllib
import urllib.request
html = "http://pudim.com.br"

try:
    site = urllib.request.urlopen(html)

except:
    print('Deu ruim!')
else:
    print('Tudo ok')
    print(site.read()) #lê o código do site todo
