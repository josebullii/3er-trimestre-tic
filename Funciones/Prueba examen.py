#Crea una función que devuelva una lista de números aleatorios que se van insertando cada medio segundo

import random
import time

def listaRandom(numElem):
    lista = []
    j = 0
    inicio = time.time()

    for i in range(0, numElem):
        j = random.randint(0, 100)
        lista.append(j)
        time.sleep(0.5)
    
    final = time.time()

    #tiempo = final - inicio
    #print(tiempo)

    return lista

#Inicio del programa

bandera = False

while bandera == False:
    try:
        numElem = int(input("¿Cuántos elementos quieres añadir?: "))
        bandera = True
    except:
        print("¡Usa un número!")
        bandera = False

print(listaRandom(numElem))