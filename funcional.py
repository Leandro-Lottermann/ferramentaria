# Aqui virá a interação com o DB e funcionalidades gerais do app.
import pandas as pd

class DBtecnicos:
    def __init__(self):
        self.df_tecnicos = pd.read_excel("funcionarios.xlsx", engine= "openpyxl") #abre arquivo

    def mostraalgo(self, cpf, nome, telefone, turno, equipe):
        dataframe = pd.DataFrame([(cpf, nome, telefone, turno, equipe)])




"""nova_linha = [(123, "alfeu", 4131, "manha", "husaaaa")]
novo_df = pd.DataFrame(nova_linha, columns=["cpf", "nome", "telefone", "turno", "equipe"]) #Cria um novo dataFrame
df_teste = pd.concat([df_teste, novo_df], ignore_index=True) #concateno, o append vai entrar em desuso futuramente.
df_teste.to_excel("funcionarios.xlsx", index = False) #sovbrescrevo o arquivo
print(df_teste)"""

