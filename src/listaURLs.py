from anytree import Node, RenderTree
import json
import requests as _requests
import bs4 as _bs4

url_base = 'http://vitibrasil.cnpuv.embrapa.br/index.php'

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

# Retirando o link base, pagina 1 e pagina 7, pois não contém aquivos para serem baixados
new_lista_link = lista_link[2: -1]

# Salvando em json a lista de links que serão usados para extrair os csv's
with open("lista_urls.json", mode="w", encoding="utf-8") as events_file:
        json.dump(new_lista_link, events_file, ensure_ascii=False)
