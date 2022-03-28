#Preguntar cuantos alumnos hay en clase
#Leer sus edades y calcular su edad media

num = int(input("¿Cuántos alumnos hay en clase?: "))
vEdades = []
sumaedades = 0

for i in range (0, num):
    edad = int(input("Indica la edad del alumno: "))
    vEdades.append[edad]
    sumaedades = vEdades[i] + sumaedades

media = sumaedades / num
print("La media de edad de los alumnos es", media)