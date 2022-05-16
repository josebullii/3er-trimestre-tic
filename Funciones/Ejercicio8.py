#Crear una función recursiva que permita calcular el factorial de un número.
#Realiza un programa principal donde se lea un entero y se muestre el resultado
#del factorial.

def factorialNum(num):
    
    factorial = 1
    
    while num > 1:
        
        factorial = factorial * num
        num = num - 1
        
    print("El factorial de", num, "es: ", factorial)
        
#Inicio del programa

num = int(input("¿A qué número quieres hacerle el factorial?: "))
factorialNum(num)