import pandas as pd

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
