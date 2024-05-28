from typing import Dict
from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import json

app = FastAPI()

with open("../src/json/Producao.json", encoding="utf-8") as events_file:
        Producao = json.load(events_file)

with open("../src/json/Comercio.json", encoding="utf-8") as events_file:
        Comercio = json.load(events_file)

with open("../src/json/ProcessaViniferas.json", encoding="utf-8") as events_file:
        ProcessaViniferas = json.load(events_file)

with open("../src/json/ProcessaAmericanas.json", encoding="utf-8") as events_file:
        ProcessaAmericanas = json.load(events_file)

with open("../src/json/ProcessaMesa.json", encoding="utf-8") as events_file:
        ProcessaMesa = json.load(events_file)

with open("../src/json/ProcessaSemclass.json", encoding="utf-8") as events_file:
        ProcessaSemclass = json.load(events_file)

with open("../src/json/ImpVinhos.json", encoding="utf-8") as events_file:
        ImpVinhos = json.load(events_file)

with open("../src/json/ImpEspumantes.json", encoding="utf-8") as events_file:
        ImpEspumantes = json.load(events_file)

with open("../src/json/ImpFrescas.json", encoding="utf-8") as events_file:
        ImpFrescas = json.load(events_file)

with open("../src/json/ImpPassas.json", encoding="utf-8") as events_file:
        ImpPassas = json.load(events_file)

with open("../src/json/ImpSuco.json", encoding="utf-8") as events_file:
        ImpSuco = json.load(events_file)

with open("../src/json/ExpVinho.json", encoding="utf-8") as events_file:
        ExpVinho = json.load(events_file)

with open("../src/json/ExpEspumantes.json", encoding="utf-8") as events_file:
        ExpEspumantes = json.load(events_file)

with open("../src/json/ExpUva.json", encoding="utf-8") as events_file:
        ExpUva = json.load(events_file)

with open("../src/json/ExpSuco.json", encoding="utf-8") as events_file:
        ExpSuco = json.load(events_file)

lista_tab = [Producao, Comercio, ProcessaViniferas, ProcessaAmericanas, ProcessaMesa, ProcessaSemclass, ImpVinhos
             , ImpEspumantes, ImpFrescas, ImpPassas, ImpSuco, ExpVinho, ExpEspumantes, ExpUva, ExpSuco]


@app.get("/")
def root():
    return {"message": "Digite '/docs' no final da barra de endereço para ver a documentação da API"}

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
