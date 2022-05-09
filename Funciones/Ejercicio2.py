#Crea un programa que pida dos número enteros al usuario y diga si alguno de
#ellos es múltiplo del otro. Crea una función EsMultiplo que reciba los dos
#números, y devuelve si el primero es múltiplo del segundo.

def esMultiplo(num1, num2):
    if num1 % num2 == 0:
        return True
    else:
        return False

#Programa principal

num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce otro número: "))

if esMultiplo(num1, num2) == True:
    print("Es múltiplo")
else:
    print("No es múltiplo")