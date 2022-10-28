import pandas as pd

arquivo = pd.read_excel("funcionarios.xlsx", engine="openpyxl")

for row in arquivo.itertuples():
    print(row)
    print(row.nome)
