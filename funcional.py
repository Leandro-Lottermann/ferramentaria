# Aqui virá a interação com o DB e funcionalidades gerais do app.
import pandas as pd

#trocar esse objeto por um objeto data frame
class DBtecnicos:
    def __init__(self):
        self.df_tecnicos = pd.read_excel("funcionarios.xlsx", engine= "openpyxl") #abre arquivo

    def add_novo_tec(self, lista_dados):
        dataframe = pd.DataFrame([lista_dados], columns=["cpf", "nome", "telefone", "turno", "equipe"]) #crio um dataframe com a tupla recebida
        df_temp = pd.concat([self.df_tecnicos, dataframe], ignore_index=True) #concateno com o dataframe do banco de dados garando um temporário
        df_temp.to_excel("funcionarios.xlsx", index=False) #aqui sobrescrevo o arquivo excel
        print(f'Técnico {lista_dados[1]} cadastrado com sucesso!')






