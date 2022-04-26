#Inicio del programa

cadena = input("Introduce una frase: ")
tam = len(cadena) - 1
i = 0
cadena2 = ""

try:
    caracter1 = input("Introduce un caracter: ")
except:
    print("¡Eso no es un caracter!")

try:
    caracter2 = input("Introduce otro caracter: ")
except:
    print("¡Eso no es un caracter!")

while i <= tam:

    if cadena[i] != caracter1:
        cadena2 = cadena2 + cadena[i]

    elif cadena[i] == caracter1:
        cadena2 = cadena2 + caracter2
    
    i = i + 1

print(cadena2)
