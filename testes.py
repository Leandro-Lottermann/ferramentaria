from datetime import datetime, timedelta
import pandas as pd

data_hoje = datetime.now()

for d in range(0, 30, 1): # usar isso para geras as colunas do dataframe
    dias = timedelta(d)
    data = data_hoje + dias
    print(data)









#no inicio criar uma lista com os parnumbers

df_1 = pd.read_excel("funcionarios.xlsx", engine= "openpyxl")
writer = pd.ExcelWriter("teste.xlsx", engine="openpyxl")
df_1.to_excel(writer, sheet_name="deu certooo3", index=False)
writer.close()
#hoje = datetime.now()
#print(format(hoje, "%d/%m/%Y"))
def ideia():
    lista_horas = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

    #vou precisar ter um iteravel com as datas ocupadas para decidir se cria uma coluna nova ou append usando o df.columns
    textoteste = "0391029,1,2,3;03913029,4,5,6" #assim que vou salvar nas linhas (as colunas serão "resdd/mm/aaaa"
    lista_reservas = textoteste.split(";")
    res_dia = []
    horas_reservadas = []
    for reserva in lista_reservas:
        res_dia.append(reserva.split(","))
        cont = 0

    for reserva in res_dia:
        horas_reservadas = horas_reservadas + reserva[1:]
    print(horas_reservadas)

    data = "07/11/2022"
    horario = 2
    data = datetime.strptime(data, "%d/%m/%Y")
    hoje = datetime.now()

    if (data-hoje).days > 30 or str(horario) in horas_reservadas: #verificação de 30 dias
        print("reserva invalida")
    else:
        print(("valido"))
    print()






#limitar

#usar o like para filtrar colunas