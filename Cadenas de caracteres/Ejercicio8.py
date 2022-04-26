#Inicio del programa

cadena = input("Introduce una frase: ")
tam = len(cadena) - 1
i = 0

while i <= tam:
    if cadena[i] == cadena[i].lower():
        print(cadena[i].upper(), end="")
    
    if cadena[i] == cadena[i].upper():
        print(cadena[i].lower(), end="")
    
    i = i + 1
