print("Introduce las siguientes notas")
parcial1 = float(input("1º Examen Parcial: "))
parcial2 = float(input("2º Examen Parcial: "))
parcial3 = float(input("3º Examen Parcial: "))

bloque = float(input("Examen final: "))
proyecto = float(input("Trabajo final: "))

parciales = ((parcial1 + parcial2 + parcial3) / 3) * 0.55
exFinal = bloque * 0.30
proyectoFinal = proyecto * 0.15

notaFinal = parciales + exFinal + proyectoFinal

print("Tu nota final de la materia será", notaFinal)