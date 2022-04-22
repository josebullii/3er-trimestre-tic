#Inicio del programa

#Introducción de los valores

numeros = (int)(input("¿Qué cantidad de númreos vas a introducir?: "))
vNum = []
numCero = 0
numMayores = 0
numMenores = 0
num = 0

for i in range(0,numeros):

    num = int(input("Introduce un número: "))
    vNum.append(num)

    if num > 0:
        numMayores = numMayores + 1
    elif num < 0:
        numMenores = numMenores + 1
    else:
        numCero = numCero + 1

print("Hay", numMayores, "números mayores de 0,", numMenores, "números menores de 0 y", numCero, "números iguales a 0")
