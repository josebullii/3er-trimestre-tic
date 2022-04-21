#Inicio del programa

#Introducción de los valores que vamos a utilizar
nota = float(input("Introduce la nota: "))
edad = int(input("Introduce la edad: "))
sexo = input("Introduce tu sexo (F = Femenino / M = Masculino): ")

#Uso de las condicionales con sus resultados correspondientes, según los valores introducidos
if nota >= 5:
    if edad >= 18:
        if sexo == "F":
            print("ACEPTADA")
        elif sexo == "M":
            print("POSIBLE")
    else:
        print("NO ACEPTADA")
else:
    print("NO ACEPTADA")

#Fin del programa