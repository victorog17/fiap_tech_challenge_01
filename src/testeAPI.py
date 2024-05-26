from typing import Union, Dict
from fastapi import FastAPI, HTTPException
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



#@app.get("/items/{item_id}")
#def read_item(item_id: int, q: Union[str, None] = None):
#    return {"item_id": item_id, "q": q}


