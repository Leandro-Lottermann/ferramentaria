import pandas as pd


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


class DBferramentas:
    def __init__(self):
        self.df_ferramentas = pd.read_excel("ferramentas.xlsx", engine="openpyxl")

    def add_nova_fer(self, lista_dados):
        dataframe = pd.DataFrame([lista_dados], columns=["ferramenta", "fabricante", "pnumber", "tamanho", "unm", "voltagem", "tipo", "material", "resmax"])
        self.df_ferramentas = pd.concat([self.df_ferramentas, dataframe], ignore_index=True)
        self.df_ferramentas.to_excel("ferramentas.xlsx", index=False)
        print(f'Ferramenta {lista_dados} cadastrado com sucesso!')


    def remove_fer(self, pnumber):

        self.df_ferramentas.drop(self.df_ferramentas.index[self.df_ferramentas["pnumber"] == pnumber].tolist(), inplace=True)
        self.df_ferramentas.reset_index(drop=True, inplace=True)
        self.df_ferramentas.to_excel("ferramentas.xlsx", index=False)

    @property
    def linhas(self):
        lista_linhas = []
        for linha in self.df_ferramentas.itertuples():
            lista_linhas.append([linha.ferramenta, linha.fabricante, linha.pnumber, linha.tamanho, linha.unm, linha.voltagem, linha.tipo, linha.material, linha.resmax])
        return lista_linhas


