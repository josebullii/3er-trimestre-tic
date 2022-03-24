#Leer lados y decir si un triangulo es isósceles, equilátero o escaleno

print("Introduce los lados de un triángulo")
lado1 = int(input("Lado 1: "))
lado2 = int(input("Lado 2: "))
lado3 = int(input("Lado 3: "))

if lado1 == lado2 and lado1 == lado3:
    print("El triángulo es equilátero")
elif (lado1 == lado2 and lado1 != lado3) or (lado1 != lado2 and lado1 == lado3):
    print("El triángulo es isósceles")
else:
    print("El triángulo es escaleno")
