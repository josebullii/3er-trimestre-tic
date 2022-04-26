#Inicio del programa

cadena = input("Introduce una frase: ")
tam = len(cadena) - 1

while tam >= 0:
    print(cadena[tam], end="")
    tam = tam - 1