print("Sistema para calcular el promedio de un alumno.")
nombre = input("Para comenzar, ¿cuál es tu nombre?: ")
nota_uno = float(input("¿Cuál es tu calificación en Matemática?: "))
nota_dos = float(input("¿Cuál es tu calificación en Química?: "))
nota_tres = float(input("¿Cuál es tu calificación en Biología?: "))
promedio = (nota_uno + nota_dos + nota_tres) / 3
#Opcional
promedio = int(promedio)

if promedio >= 15 :
    print("Felicidades " + nombre + " aprobaste la materia con un promedio de", promedio)
    print("Felicidades " + nombre + " aprobaste la materia con un promedio de", round(promedio,2))
else: 
    print("Lo sentimos " + nombre + " desaprobaste la materia con un promedio de", promedio)
    print("Lo sentimos " + nombre + " desaprobaste la materia con un promedio de", round(promedio,2))
print("¡Feliz año nuevo!")