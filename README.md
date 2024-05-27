# Fiap Tech Challenge 01
## API Banco de dados de uva, vinho e derivados

### Descrição
Está API foi desenvolvida para retornar os dados sobre vitivicultura disponiveis no site da [Embrapa](http://vitibrasil.cnpuv.embrapa.br/).
A API fornece acesso as categorias de produção, processamento, comercialização, importação e exportação de uvas, vinhos e derivados.
O objetivo da API é exibir os dados da categoria desejada.

### Projeto

Os arquivos do projeto estão estruturados da seguinte forma:

- testeAPI.py: Arquivo principal que lê arquivos JSON e roda a API.
- listaURLs.py: Arquivo com o objetivo de extrair os links que contém os dados em CSV das categorias do site da Embrapa.
- scrapper.py: Arquivo que baixa o conteúdo CSV dos links gerados em listaURLs.py e salva na pasta src/csv para organização.
- tabelas.py: Arquivo destinado a ler os arquivos CSV baixados e salva-los em JSON na pasta src/json para melhor leitura dos dados na API.
- lista_urls.json: Arquivo gerado por listaURLs.py com todos os links das categorias que contém arquivos csv.

### Referencia Tabelas

- Categoria Produção: Producao.csv
- Categoria Processamento:
  - Subcategoria Viníferas: ProcessaViniferas.csv
  - Subcategoria Americanas e híbridas: ProcessaAmericanas.csv
  - Subcategoria Uvas de mesa: ProcessaMesa.csv
  - Subcategoria Sem classificação: ProcessaSemclass.csv
- Categoria Comercialização: Comercio.csv
- Categoria Importação:
  - Subcategoria Vinhos de mesa: ImpVinhos.csv
  - Subcategoria Espumantes: ImpEspumantes.csv
  - Subcategoria Uvas frescas: ImpFrescas.csv
  - Subcategoria Uvas passas: ImpPassas.csv
  - Subcategoria Suco de uva: ImpSuco.csv
- Categoria Exportação:
  - Subcategoria Vinhos de mesa: ExpVinho.csv
  - Subcategoria Espumantes: ExpEspumantes.csv
  - Subcategoria Uvas frescas: ExpUva.csv
  - Subcategoria Suco de uva: ExpSuco.csv

### Proposta de Arquitetura
  ![alt text](plano_arquitetura.jpeg)