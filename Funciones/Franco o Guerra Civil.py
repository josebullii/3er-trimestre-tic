#Inicio del programa
import random

#Va a devolver el nombre con más probabilidad: Franco o Guerra Civil

def francoVSguerracivil(ite): #ite es el número de interacciones
    #Inicializar de variables
    opc1 = "El tema a desarrollar en el examen será Franco"
    opc2 = "El tema a desarrollar en el examen será la Guerra Civil"
    numFranco = 0
    numGuerra = 0
    contador = 0

    #Bucle para saber el número de probabilidad de cada variable
    for i in range(0, ite):
        numRandom = random.randint(1,2)

        if numRandom == 1:
            numFranco = numFranco + 1
        elif numRandom == 2:
            numGuerra = numGuerra + 1

        contador = contador + 1

    #Probabilidad de cada tema
    probFranco = (numFranco / contador) * 100
    probGuerra = (numGuerra / contador) * 100

    #Visualización del porcentaje
    #print("La probabilidad de Franco es del", probFranco, "%")
    #print("La probabilidad de la Guerra Civil es del", probGuerra, "%")

    #Devolución de valores
    if probFranco > probGuerra:
        return opc1
    elif probFranco < probGuerra:
        return opc2

print(francoVSguerracivil(10079))