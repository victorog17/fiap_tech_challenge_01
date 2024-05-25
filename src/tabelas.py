import pandas as pd
from typing import Dict
import json as _json

#tabela_extraida = pd.read_csv('Comercio.csv', sep=';')
#print(tabela_extraida.head())
#
#data_dict = tabela_extraida.to_dict(orient="records")
#print(data_dict)

producao = pd.read_csv("Producao.csv", sep=';')
comercio = pd.read_csv("Comercio.csv", sep=';')

comercio.to_json("Comercio.json")
producao.to_json("Producao.json")

#producao_dict = producao.to_dict(orient="records")
#comercio_dict = comercio.to_dict(orient="records")
#print(producao_dict)
#print('-'*50)
#print(comercio_dict)
#
#lista_tab = [producao_dict, comercio_dict]
#print('-'*50)
#print(lista_tab)
