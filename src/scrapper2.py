from typing import List
import requests as _requests
import bs4 as _bs4
import urllib.request as urlilb
import re

url_base = 'http://vitibrasil.cnpuv.embrapa.br/'
url = 'http://vitibrasil.cnpuv.embrapa.br/?opcao=opt_04'

variavel_paginas = ['?opcao=opt_02', '?opcao=opt_03', '?opcao=opt_04', '?opcao=opt_05', '?opcao=opt_06']

def encontrar_arquivos_todas_paginas():
    pass


def encontrar_arquivos_tabelas_por_pagina(url, url_base):

    response = _requests.get(url)
    soup = _bs4.BeautifulSoup(response.content, "html.parser")

    urls = []
    for i in soup.find_all(class_="footer_content", href=True):
        href = i['href']
        if href.endswith('.csv'):
            if href.startswith('http'):
                print(href)
            else:
                url_dowload = url_base + href
                urls.append(url_dowload)
                print(url_dowload)
    return urls[0]

lista_downloads = []
for j in variavel_paginas:
    url_pagina = url_base + j
    print(url_pagina)
    teste_funcao = encontrar_arquivos_tabelas_por_pagina(url_pagina, url_base)
    lista_downloads.append(teste_funcao)
    print(teste_funcao)    

print('-'*50)
print(lista_downloads)
print('-'*50)

for i in lista_downloads:
    match = re.search(r'/(\w+)\.csv$', i)
    print(match)
    nome = match.group(1)
    urlilb.urlretrieve(i, f'{nome}.csv')

#teste_funcao = encontrar_arquivos_tabelas_por_pagina(url, url_base)
#print(teste_funcao)
#
#for i in teste_funcao:
#    match = re.search(r'/(\w+)\.csv$', i)
#    print(match)
#    nome = match.group(1)
#    urlilb.urlretrieve(i, f'{nome}.csv')
