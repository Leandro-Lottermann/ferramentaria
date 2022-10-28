import pandas as pd

arquivo = pd.read_excel("funcionarios.xlsx", engine="openpyxl")

print(arquivo)
print("-"*20)
cpf = 232122
arquivo.drop(arquivo.index[arquivo["cpf"] == cpf].tolist(), inplace=True)
arquivo.reset_index(drop=True, inplace=True)
print("-"*20)
print(arquivo)
#938123
#232122
