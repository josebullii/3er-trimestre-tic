from math import sqrt

print("Indica la medida de los lados del triángulo")
lado1 = int(input("Lado 1: "))
lado2 = int(input("Lado 2: "))
lado3 = int(input("Lado 3: "))

base = int(input("¿Cuánto vale la base?: "))
altura = int(input("¿Cuánto vale la altura?: "))

perimetro = lado1 + lado2 + lado3
area = (base * altura) / 2

print("El perímetro del triángulo es", perimetro, "y el área es", area)