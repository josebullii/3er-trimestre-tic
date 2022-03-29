print("Introduce los datos del punto X")
x1 = int(input("x1: "))
x2 = int(input("x2: "))

print("Introduce los datos del punto Y")
y1 = int(input("y1: "))
y2 = int(input("y2: "))

distancia = (((abs(x1 - x2)) ** 2) + ((abs(y1 - y2)) ** 2)) ** 0.5

print("La distancia entre dos puntos es", distancia)