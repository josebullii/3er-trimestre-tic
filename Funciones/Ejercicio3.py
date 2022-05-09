#Crear una función que calcule la temperatura media de un día a partir de la
#temperatura máxima y mínima. Crear un programa principal, que utilizando la
#función anterior, vaya pidiendo la temperatura máxima y mínima de cada día y
#vaya mostrando la media. El programa pedirá el número de días que se van a
#introducir.

def tempMedia(dias):
    tempMax = 0
    tempMin = 0
    suma = 0
    media = 0

    for i in range(0, dias):
        tempMax = int(input("Introduce la temperatura máxima del día: "))
        tempMin = int(input("Introduce la temperatura mínima del día: "))
        suma = tempMax + tempMin
        media = (int)(suma / 2)
        print("La temperatura media ha sido de: ", media, "\n")


#Programa principal

dias = int(input("¿De cuántos días vas a introducir los valores?: "))
tempMedia(dias)