#Realizar un programa que compruebe si una cadena contiene una subcadena.
#Las dos cadenas se introducen por teclado.

#Introducción de variables
cadena = input("Introduce una frase: ")
subcadena = input("Introduce la palabra que quieres buscar: ")

posicion = cadena.find(subcadena) #Primera posición en la que se encuentra la palabra

if posicion >= 0:
    print("La palabra se encuentra en el texto y está situada en la posición", posicion)
else:
    print("La palabra no se encuentra en el texto")