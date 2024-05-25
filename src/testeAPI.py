from typing import Union
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
import pandas as pd
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import json as _json

app = FastAPI()

with open("Producao.json", encoding="utf-8") as events_file:
        data = _json.load(events_file)

with open("Comercio.json", encoding="utf-8") as events_file:
        data2 = _json.load(events_file)

lista_tab = [data, data2]


@app.get("/")
def read_root():
    tabela=pd.read_csv("Producao.csv")
    #print(tabela.head())
    json_compatible_item_data = jsonable_encoder(tabela)
    return JSONResponse(content=lista_tab)


#@app.get("/processamento/{name}")
#def read_processamento(name: str):
#    if name == 1:
#        tabela=pd.read_csv("ProcessaViniferas.csv")
#    tabela=pd.read_csv("Comercio.csv")
#    #print(tabela.head())
#    json_compatible_item_data = jsonable_encoder(tabela)
#    return JSONResponse(content=json_compatible_item_data)











#@app.get("/items/{item_id}")
#def read_item(item_id: int, q: Union[str, None] = None):
#    return {"item_id": item_id, "q": q}


