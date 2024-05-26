import requests as requests
import bs4 as bs4
import urllib.request as urlilb
import re
import json

url_base = 'http://vitibrasil.cnpuv.embrapa.br/'

def encontrar_arquivos_tabelas_por_pagina(url, url_base):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content, "html.parser")

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

# abre o arquivo json criado no script listaURLs.py
with open("lista_urls.json", encoding="utf-8") as events_file:
        lista_paginas = json.load(events_file)

print(lista_paginas)

# Faz a coleta e baixa o conteudo csv dos links existentes no arquivo json lido
lista_downloads = []
for j in lista_paginas:
    url_pagina = j
    teste_funcao = encontrar_arquivos_tabelas_por_pagina(url_pagina, url_base)
    lista_downloads.append(teste_funcao)

for i in lista_downloads:
    match = re.search(r'/(\w+)\.csv$', i)
    print(match)
    nome = match.group(1)
    urlilb.urlretrieve(i, f'../src/csv/{nome}.csv')
