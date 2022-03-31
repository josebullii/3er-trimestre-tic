minutos = int(input("Indica la cantidad de minutos empleados: "))

horaExacta = minutos / 60
horas = "{:.0f}".format(horaExacta)

print("Has dedicado alrededor de", horas, "horas")