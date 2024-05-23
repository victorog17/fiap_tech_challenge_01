from typing import Union
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
import pandas as pd
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def read_root():
    tabela=pd.read_csv("Producao.csv")
    #print(tabela.head())
    json_compatible_item_data = jsonable_encoder(tabela)
    return JSONResponse(content=json_compatible_item_data)











#@app.get("/items/{item_id}")
#def read_item(item_id: int, q: Union[str, None] = None):
#    return {"item_id": item_id, "q": q}


