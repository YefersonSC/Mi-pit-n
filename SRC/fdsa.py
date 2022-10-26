nota1 = float(input("Inserte la nota 1: "))
if nota1 < 0 or nota1 > 20:
    exit("Nota no disponible")
nota2 = float(input("Inserte la nota 2: "))
if nota2 < 0 or nota2 > 20:
    exit("Nota no disponible")
nota3 = float(input("Inserte la nota 3: "))
if nota3 < 0 or nota3 > 20:
    exit("Nota no disponible")
promedio = (nota1 + nota2 + nota3)/3

if promedio >= 13.5:
    print("Has aprobado")
elif 8.5 <= promedio < 13.5:
    print("Has desaprobado")
else:
    print("Has reprobado")