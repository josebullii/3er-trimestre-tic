#Uso del bucle for

sumapares = 0
sumaimpares = 0

for i in range (11):
    if i % 2 == 0:
        sumapares = sumapares + i
    elif i % 2 != 0:
        sumaimpares = sumaimpares + i
    
print("La suma de los números pares es", sumapares)
print("La suma de los números impares es", sumaimpares)