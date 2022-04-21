#Inicio del programa

#Introducción de los valores
precioInicial = float(input("Introduce el precio inicial del kilo de uva: "))
precioFinal = 0
tipo = input("Introduce el tipo de uva (A o B): ")
tamaño = int(input("Introduce el tamaño de la uva (1 o 2): "))

if tipo == "A":
    if tamaño == 1:
        precioFinal = precioInicial + 0.20 # +20 centimos por su tamaño
    elif tamaño == "2":
        precioFinal = precioInicial + 0.30 # +30 centimos por su tamaño

if tipo == "B":
    if tamaño == 1:
        precioFinal = precioInicial - 0.30 # -30 centimos por su tamaño
    elif tamaño == "2":
        precioFinal = precioInicial - 0.50 # -50 centimos por su tamaño

#Final del programa
