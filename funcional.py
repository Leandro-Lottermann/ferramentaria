# Aqui virá a interação com o DB e funcionalidades gerais do app.
import pandas as pd

#trocar esse objeto por um objeto data frame
class DBtecnicos:
    def __init__(self):
        self.df_tecnicos = pd.read_excel("funcionarios.xlsx", engine= "openpyxl") #abre arquivo

    def add_novo_tec(self, lista_dados):
        dataframe = pd.DataFrame([lista_dados], columns=["cpf", "nome", "telefone", "turno", "equipe"]) #crio um dataframe com a tupla recebida
        self.df_tecnicos = pd.concat([self.df_tecnicos, dataframe], ignore_index=True) #concateno com o dataframe do banco de dados garando um temporário
        self.df_tecnicos.to_excel("funcionarios.xlsx", index=False) #aqui sobrescrevo o arquivo excel
        print(f'Técnico {lista_dados[1]} cadastrado com sucesso!')

    def remove_tec(self, cpf):

        self.df_tecnicos.drop(self.df_tecnicos.index[self.df_tecnicos["cpf"] == cpf].tolist(), inplace=True)
        self.df_tecnicos.reset_index(drop=True, inplace=True)
        self.df_tecnicos.to_excel("funcionarios.xlsx", index=False)

    @property
    def linhas(self):
        lista_linhas = []
        for linha in self.df_tecnicos.itertuples():
            lista_linhas.append([linha.cpf, linha.nome, linha.telefone, linha.turno, linha.equipe])
        return lista_linhas





