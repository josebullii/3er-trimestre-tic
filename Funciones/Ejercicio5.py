#Crea una función “calcularMaxMin” que recibe una arreglo con valores numérico 
#y devuelve el valor máximo y el mínimo. Crea un programa que pida números 
#por teclado y muestre el máximo y el mínimo, utilizando la función anterior.

def calcularMaxMin(listaNum):
    numMax = 0
    numMin = 0
    aux = listaNum[0]
    
    for i in listaNum:
        if i > aux:
            aux = i
        numMax = aux
        
    for i in listaNum:
        if i < aux:
            aux = i
        numMin = aux
        
    print("El número mayor es: ", numMax)
    print("El número menor es: ", numMin)
    
    
#Inicio del programa

listaNum = []
numValores = int(input("¿Cuántos valores vas a introducir?: "))

for i in range(0, numValores):
    num = int(input("Introduce un valor: "))
    listaNum.append(num)
    
calcularMaxMin(listaNum)