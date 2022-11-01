from datetime import datetime

lista_horas = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]


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

if (data-hoje).days > 30 or str(horario) in horas_reservadas:
    print("reserva invalida")
else:
    print(("valido"))
print()






#limitar

#usar o like para filtrar colunas