import pandas as pd

tabela_extraida = pd.read_csv('..\\src2\\Producao.csv', sep=';')
print(tabela_extraida.head())