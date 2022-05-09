#Crea un procedimiento EscribirCentrado, que reciba como parámetro un texto y
#lo escriba centrado en pantalla (suponiendo una anchura de 80 columnas; pista:
#deberás escribir 40 - longitud/2 espacios antes del texto). Además subraya el
#mensaje utilizando el carácter =.

#Inicio del programa

#Función
def escribirCentrado(texto, tam):
    numEspacios = (int)(90 - (tam / 2))
    textoCentrado = ""

    for i in range(0, numEspacios):
        textoCentrado = textoCentrado + " "

    print(textoCentrado + texto)


#Programa principal
#Introducción del texto que va a recibir el procedimiento
texto = input("Introduce una oración: ")
tam = len(texto)

escribirCentrado(texto, tam)