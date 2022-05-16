#Crear una función que calcule el MCD de dos número por el método de Euclides.
#El método de Euclides es el siguiente:
# Se divide el número mayor entre el menor.
# Si la división es exacta, el divisor es el MCD.
# Si la división no es exacta, dividimos el divisor entre el resto obtenido y se
#continúa de esta forma hasta obtener una división exacta, siendo el último
#divisor el MCD.
#Crea un programa principal que lea dos números enteros y muestre el MCD.


def calcMCD(num1, num2):
    MCD = 0
    numMay = 0
    numMin = 0
    
    if num1 > num2:
        numMay = num1
        numMin = num2
    else:
        numMin = num1
        numMay = num2
    
    dividendo = numMay
    divisor = numMin
    cociente = dividendo / divisor
    resto = numMay % numMin
    
    if resto == 0:
        MCD = divisor
        
    else:
        while resto != 0:
            divisor = divisor / resto
            resto = divisor % resto
    
    print("El MCD es", divisor)
    
    
#Inicio del programa

num1 = int(input("Introduce un número entero: "))
num2 = int(input("Introduce otro número entero: "))
calcMCD(num1, num2)