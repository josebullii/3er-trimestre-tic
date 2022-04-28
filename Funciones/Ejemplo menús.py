#Crea un procedimiento que pinte un menú

def mostrarMenu():

    opcion = 0

    while (opcion < 1) or (opcion > 6):
        print("1 - Añadir contacto")
        print("2 - Editar contacto")
        print("3 - Salir")
        print("")

        try:
            opcion = int(input("Selecciona una opción: "))
        except:
            opcion = 0
            print("No es correcto")

        if (opcion < 1) or (opcion > 3):
            print("")
            print("Las opciones son 1, 2 y 3")
            print("")

    return opcion

mostrarMenu()