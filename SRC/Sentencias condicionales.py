print("Sistema para calcular el promedio de un alumno.")
nombre = input("Para comenzar, ¿cúal es tu nombre?: ")
nota_uno = float(input("¿Cuál es tu calificación en Matemática?, " + nombre + ": " ))
nota_dos = float(input("¿Cuál es tu calificación en Química?, " + nombre + ": "))
if (nota_uno + nota_dos) / 2 > 14 :
    print("Felicidades aprobaste el curso con un promedio de: ", (nota_uno + nota_dos) / 2)
print("Fin.")