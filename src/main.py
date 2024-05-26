from anytree import Node, RenderTree
import json
from typing import Dict
import requests as _requests
import bs4 as _bs4
import urllib.request as urlilb
import re
import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel


# Inicio listagem de URLs
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

print("Fim coletade URLs")
# Fim listagem de URLs

# Inicio Scrapper

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

# abre o arquivo json criado no script listaURLs.py
with open("lista_urls.json", encoding="utf-8") as events_file:
        lista_paginas = json.load(events_file)

print(lista_paginas)

# Faz a coleta e baixa o conteudo csv dos links existentes no arquivo json lido
lista_downloads = []
for j in lista_paginas:
    #url_pagina = url_base + j
    url_pagina = j
    #print(url_pagina)
    teste_funcao = encontrar_arquivos_tabelas_por_pagina(url_pagina, url_base)
    lista_downloads.append(teste_funcao)
    #print(teste_funcao)    

for i in lista_downloads:
    match = re.search(r'/(\w+)\.csv$', i)
    print(match)
    nome = match.group(1)
    urlilb.urlretrieve(i, f'{nome}.csv')

print("Fim coletade arquivos CSV")
# Fim Scrapper

# Inicio Leitura CSV e salvamento em JSON

# Leitura CSVs
producao = pd.read_csv("Producao.csv", sep=';')
processa_viniferas = pd.read_csv("ProcessaViniferas.csv", sep='\t')
processa_americanas = pd.read_csv("ProcessaAmericanas.csv", sep='\t')
processa_mesa = pd.read_csv("ProcessaMesa.csv", sep='\t')
processa_semclass = pd.read_csv("ProcessaSemclass.csv", sep='\t')
comercio = pd.read_csv("Comercio.csv", sep=';')
imp_vinhos = pd.read_csv("ImpVinhos.csv", sep=';')
imp_espumantes = pd.read_csv("ImpEspumantes.csv", sep=';')
imp_frescas = pd.read_csv("ImpFrescas.csv", sep=';')
imp_passas = pd.read_csv("ImpPassas.csv", sep=';')
imp_sucos = pd.read_csv("ImpSuco.csv", sep=';')
exp_vinhos = pd.read_csv("ExpVinho.csv", sep=';')
exp_espumantes = pd.read_csv("ExpEspumantes.csv", sep=';')
exp_uva = pd.read_csv("ExpUva.csv", sep=';')
exp_suco = pd.read_csv("ExpSuco.csv", sep=';')

# Conversao para JSON
comercio.to_json("Comercio.json")
processa_viniferas.to_json("ProcessaViniferas.json")
processa_americanas.to_json("ProcessaAmericanas.json")
processa_mesa.to_json("ProcessaMesa.json")
processa_semclass.to_json("ProcessaSemclass.json")
producao.to_json("Producao.json")
imp_vinhos.to_json("ImpVinhos.json")
imp_espumantes.to_json("ImpEspumantes.json")
imp_frescas.to_json("ImpFrescas.json")
imp_passas.to_json("ImpPassas.json")
imp_sucos.to_json("ImpSuco.json")
exp_vinhos.to_json("ExpVinho.json")
exp_espumantes.to_json("ExpEspumantes.json")
exp_uva.to_json("ExpUva.json")
exp_suco.to_json("ExpSuco.json")

print("Fim coletade arquivos formato JSON")
# Fim Leitura CSV e salvamento em JSON

# Inicio FastAPI

app = FastAPI()

with open("Producao.json", encoding="utf-8") as events_file:
        Producao = json.load(events_file)

with open("Comercio.json", encoding="utf-8") as events_file:
        Comercio = json.load(events_file)

with open("ProcessaViniferas.json", encoding="utf-8") as events_file:
        ProcessaViniferas = json.load(events_file)

with open("ProcessaAmericanas.json", encoding="utf-8") as events_file:
        ProcessaAmericanas = json.load(events_file)

with open("ProcessaMesa.json", encoding="utf-8") as events_file:
        ProcessaMesa = json.load(events_file)

with open("ProcessaSemclass.json", encoding="utf-8") as events_file:
        ProcessaSemclass = json.load(events_file)

with open("ImpVinhos.json", encoding="utf-8") as events_file:
        ImpVinhos = json.load(events_file)

with open("ImpEspumantes.json", encoding="utf-8") as events_file:
        ImpEspumantes = json.load(events_file)

with open("ImpFrescas.json", encoding="utf-8") as events_file:
        ImpFrescas = json.load(events_file)

with open("ImpPassas.json", encoding="utf-8") as events_file:
        ImpPassas = json.load(events_file)

with open("ImpSuco.json", encoding="utf-8") as events_file:
        ImpSuco = json.load(events_file)

with open("ExpVinho.json", encoding="utf-8") as events_file:
        ExpVinho = json.load(events_file)

with open("ExpEspumantes.json", encoding="utf-8") as events_file:
        ExpEspumantes = json.load(events_file)

with open("ExpUva.json", encoding="utf-8") as events_file:
        ExpUva = json.load(events_file)

with open("ExpSuco.json", encoding="utf-8") as events_file:
        ExpSuco = json.load(events_file)

lista_tab = [Producao, Comercio, ProcessaViniferas, ProcessaAmericanas, ProcessaMesa, ProcessaSemclass, ImpVinhos
             , ImpEspumantes, ImpFrescas, ImpPassas, ImpSuco, ExpVinho, ExpEspumantes, ExpUva, ExpSuco]

@app.get("/")
def root():
    return {"message": "welcome to this cool historical events api"}

@app.get("/all_tables")
def all_tables():
    return lista_tab

@app.get("/producao")
def get_producao() -> Dict:
        return Producao

@app.get("/comercio")
def get_comercio() -> Dict:
        return Comercio

@app.get("/processamento", description="Escolha 1: Viníferas, 2: Americanas e híbridas, 3: Uvas de mesa, 4: Sem classificação")
def get_processamento(subcategoria: str) -> Dict:
        if subcategoria == "1":
                data = ProcessaViniferas
        elif subcategoria == "2":
                data = ProcessaAmericanas
        elif subcategoria == "3":
                data = ProcessaMesa
        elif subcategoria == "4":
                data = ProcessaSemclass
        else:
                raise HTTPException(status_code=500, detail="This is not a option")
        return data

@app.get("/importacao", description="Escolha 1: Vinhos de mesa, 2: Espumantes, 3: Uvas frescas, 4: Uvas passas, 5: Suco de uva")
def get_importacao(subcategoria: str) -> Dict:
        if subcategoria == "1":
                data = ImpVinhos
        elif subcategoria == "2":
                data = ImpEspumantes
        elif subcategoria == "3":
                data = ImpFrescas
        elif subcategoria == "4":
                data = ImpPassas
        elif subcategoria == "5":
                data = ImpSuco
        else:
                raise HTTPException(status_code=500, detail="This is not a option")
        return data

@app.get("/exportacao", description="Escolha 1: Vinhos de mesa, 2: Espumantes, 3: Uvas frescas, 4: Suco de uva")
def get_exportacao(subcategoria: str) -> Dict:
        if subcategoria == "1":
                data = ExpVinho
        elif subcategoria == "2":
                data = ExpEspumantes
        elif subcategoria == "3":
                data = ExpUva
        elif subcategoria == "4":
                data = ExpSuco
        else:
                raise HTTPException(status_code=500, detail="This is not a option")
        return data

# Fim FastAPI