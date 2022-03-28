salariobase = int(input("Indica tu salario base: "))
numeroventas = int(input("Indica el número de ventas realizadas este mes: "))

comision = salariobase * 0.1

total = salariobase + (comision * numeroventas)

print("Has obtenido un total de", total, "euros este mes")