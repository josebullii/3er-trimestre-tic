#Inicio del programa

cadena = input("Dime una cadena: ")
subcadena = input("Dime una subcadena: ")

if (subcadena == cadena[0:len(subcadena)]):
    print("La cadena leía por teclado SÍ comienza por la subcadena introducida por teclado")

else:
    print("La cadena leía por teclado NO comienza por la subcadena introducida por teclado")