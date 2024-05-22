from typing import List
import requests as _requests
import bs4 as _bs4
import urllib.request as urlilb
import re

url_base = 'http://vitibrasil.cnpuv.embrapa.br/'
#url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02'
url = 'http://vitibrasil.cnpuv.embrapa.br/?opcao=opt_02'

response = _requests.get(url)
#print(response.status_code)
soup = _bs4.BeautifulSoup(response.content, "html.parser")
#print(soup)
print('-'*50)
print(soup.find_all("button", value="opt_02"))
print('-'*50)
#print(soup)
urls = []
#for i in soup.find_all("a", href=True):
for i in soup.find_all(class_="footer_content", href=True):
    href = i['href']
    if href.endswith('.csv'):
        if href.startswith('http'):
            print(href)
        else:
            teste = url_base + href
            urls.append(teste)
            print(teste)


print(urls[0])
match = re.search(r'/(\w+)\.csv$', urls[0])
print(match)
nome = match.group(1)
urlilb.urlretrieve(urls[0], f'{nome}.csv')
