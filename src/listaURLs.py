from anytree import Node, RenderTree
import json

#udo = Node("Udo")
#marc = Node("Marc", parent=udo)
#lian = Node("Lian", parent=marc)
#dan = Node("Dan", parent=udo)
#jet = Node("Jet", parent=dan)
#jan = Node("Jan", parent=dan)
#joe = Node("Joe", parent=dan)

#print(udo)
#Node('/Udo')
#print(joe)
#Node('/Udo/Dan/Joe')

#for pre, fill, node in RenderTree(udo):
#    print("%s%s" % (pre, node.name))

#print(dan.children)

from typing import List
import requests as _requests
import bs4 as _bs4
import urllib.request as urlilb
import re



url_base = 'http://vitibrasil.cnpuv.embrapa.br/index.php'
#url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02'
url = 'http://vitibrasil.cnpuv.embrapa.br/?opcao=opt_02'


raiz = Node(url_base)
response = _requests.get(url_base)
soup = _bs4.BeautifulSoup(response.content, "html.parser")

for i in soup.find_all("button"):
    if i["name"]=="opcao": 
        #print(i)
        folhaNivel1=Node(url_base+"?opcao="+i["value"],parent=raiz)
        responseNivel1 = _requests.get(url_base+"?opcao="+i["value"])
        soupNivel1 = _bs4.BeautifulSoup(responseNivel1.content, "html.parser")
        
        for j in soupNivel1.find_all("button"):
            try:
                if j["name"]=="subopcao":
                    folhaNivel2=Node(url_base+"?subopcao="+j["value"]+"&opcao="+i["value"],parent=folhaNivel1)
                    responseNivel2 = _requests.get(url_base+"?subopcao="+j["value"]+"&opcao="+i["value"])
                    soupNivel2 = _bs4.BeautifulSoup(responseNivel2.content, "html.parser")
            except: 
                print("Botao sem nome!")
            
        

lista_link = []
for pre, fill, node in RenderTree(raiz):
    lista_link.append(node.name)
    print("%s%s" % (pre, node.name))

print('-'*50)
print(lista_link)
print('-'*50)
for i in lista_link:
    print(i)
print('-'*50)
#lista_link.pop(0)
new_lista_link = lista_link[2: -1]
print(new_lista_link)
print('-'*50)
print(type(new_lista_link))
for i in new_lista_link:
    print(i)

with open("lista_urls.json", mode="w", encoding="utf-8") as events_file:
        json.dump(new_lista_link, events_file, ensure_ascii=False)

#for i in soup.find_all(class_="footer_content", href=True):
#    href = i['href']
#    if href.endswith('.csv'):
#        if href.startswith('http'):
#            print(href)
#        else:
#            teste = url_base + href
#            urls.append(teste)
#            print(teste)


#print(urls[0])
#match = re.search(r'/(\w+)\.csv$', urls[0])
#print(match)
#nome = match.group(1)
#urlilb.urlretrieve(urls[0], f'{nome}.csv')
