#Introducir una cadena de caracteres e indicar si es un palíndromo. 
#Una palabra palíndroma es aquella que se lee igual adelante que atrás.ç

#Introducción de la variable
palabra = input("Introduce una palabra: ")
subcadena = ""
tam = len(palabra) - 1

for i in reversed(palabra):
    subcadena = subcadena + i

if palabra == subcadena:
    print("La palabra es un palíndromo")
else:
    print("No es un palíndromo")