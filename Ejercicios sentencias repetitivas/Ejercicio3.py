#Inicio del programa

#Introducción de los valores

num = 1 #Inicialización a un número para entrar al bucle
total = 0 #Inicialización de la suma de los números que vamos a introducir
contador = 0 #Contador para saber la cantidad de números introducidos para hacer la media

while num != 0: #Uso del bucle while para repetir la acción
    num = int(input("Introduce números (0 para salir): "))
    total = num + total
    contador = contador + 1


print("La suma de todos los números introducidos es:", total)

media = total / contador #Media aritmética de los números introducidos
print("La media de los números introducidos es:", media)

#Fin del programa