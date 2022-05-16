#Diseñar una función que calcule el área y el perímetro de una circunferencia. 
#Utiliza dicha función en un programa principal que lea el radio de una 
#circunferencia y muestre su área y perímetro.

import math

def areaPerimetro(radio):
    numeroPi = math.pi
    
    area = numeroPi * (radio**2)
    perimetro = 2 * numeroPi * radio
    
    print("El área de la circunferencia es: ", area)
    print("El perímetro de la circunferencia es: ", perimetro)
    
#Inicio del programa

radio = int(input("Indica el radio de la circunferencia: "))

areaPerimetro(radio)