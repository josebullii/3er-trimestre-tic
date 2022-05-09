def pintaMenu():

    print("")
    print("1 - Añadir contacto")
    print("2 - Editar contacto")
    print("3 - Salir")
    print("")


def seleccionOpcion():

    pintaMenu()

    opcion = 0
    while (opcion < 1) or (opcion > 3):
        opcion = int(input("Dime una opción: "))

        if (opcion < 1) or (opcion > 3):
            print("Selección incorrecta\n")

    return opcion

def programa():
    print("***** Ejercicios de funciones *****")
    opc = 0

    while opc != 3:
        opc = seleccionOpcion()
        match opc:
            case 1:
                print("Ejercicio 1")
            case 2:
                print("Ejercicio 2")
            case 3: 
                print ("Saliendo del programa...")



programa()