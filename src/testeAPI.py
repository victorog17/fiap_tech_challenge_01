from typing import Union, Dict
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
import pandas as pd
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import json as _json

app = FastAPI()

with open("Producao.json", encoding="utf-8") as events_file:
        Producao = _json.load(events_file)

with open("Comercio.json", encoding="utf-8") as events_file:
        Comercio = _json.load(events_file)

with open("ProcessaViniferas.json", encoding="utf-8") as events_file:
        ProcessaViniferas = _json.load(events_file)

with open("ProcessaAmericanas.json", encoding="utf-8") as events_file:
        ProcessaAmericanas = _json.load(events_file)

with open("ProcessaMesa.json", encoding="utf-8") as events_file:
        ProcessaMesa = _json.load(events_file)

with open("ProcessaSemclass.json", encoding="utf-8") as events_file:
        ProcessaSemclass = _json.load(events_file)

with open("ImpVinhos.json", encoding="utf-8") as events_file:
        ImpVinhos = _json.load(events_file)

with open("ImpEspumantes.json", encoding="utf-8") as events_file:
        ImpEspumantes = _json.load(events_file)

with open("ImpFrescas.json", encoding="utf-8") as events_file:
        ImpFrescas = _json.load(events_file)

with open("ImpPassas.json", encoding="utf-8") as events_file:
        ImpPassas = _json.load(events_file)

with open("ImpSuco.json", encoding="utf-8") as events_file:
        ImpSuco = _json.load(events_file)

with open("ExpVinho.json", encoding="utf-8") as events_file:
        ExpVinho = _json.load(events_file)

with open("ExpEspumantes.json", encoding="utf-8") as events_file:
        ExpEspumantes = _json.load(events_file)

with open("ExpUva.json", encoding="utf-8") as events_file:
        ExpUva = _json.load(events_file)

with open("ExpSuco.json", encoding="utf-8") as events_file:
        ExpSuco = _json.load(events_file)

lista_tab = [Producao, Comercio, ProcessaViniferas, ProcessaAmericanas, ProcessaMesa, ProcessaSemclass, ImpVinhos
             , ImpEspumantes, ImpFrescas, ImpPassas, ImpSuco, ExpVinho, ExpEspumantes, ExpUva, ExpSuco]


@app.get("/")
def read_root():
    tabela=pd.read_csv("Producao.csv")
    #print(tabela.head())
    json_compatible_item_data = jsonable_encoder(tabela)
    return JSONResponse(content=lista_tab)

@app.get("/producao")
def get_producao(ano: str) -> Dict:
    data = Producao[ano]
    return data

@app.get("/comercio")
def get_comercio(ano: str) -> Dict:
    data = Comercio[ano]
    return data

#@app.get("/processamento", description="Escolha 1: Viníferas, 2: Americanas e híbridas, 3: Uvas de mesa, 4: Sem classificação")
#def get_processamento(subcategoria: str, ano: str) -> Dict:
#    try:
#        if subcategoria == "1":
#            data = ProcessaViniferas[ano]
#        elif subcategoria == "2":
#            data = ProcessaAmericanas[ano]
#        elif subcategoria == "3":
#            data = ProcessaMesa[ano]
#        elif subcategoria == "4":
#            data = ProcessaSemclass[ano]
#        return data
#    except Exception:
#        return "This is not a option"



#@app.get("/items/{item_id}")
#def read_item(item_id: int, q: Union[str, None] = None):
#    return {"item_id": item_id, "q": q}


