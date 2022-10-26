print(" este es un sistema para sacar el promedio de un alumno")
nombre=input("para comenzar ,¿cul es tu nombre ?: ")
algebra=float(input("¿cual es tu calificacion en algebra ?:"))
trigonometria=float(input("¿cual es tu calificacion en trigonometria ? : "))
aritmetica=float(input("¿cual es tu calificacion en aritmetica? : "))
geometria =float(input("¿cual es tu calificacion en geometria ? : "))
promedio= (algebra + trigonometria + aritmetica + geometria ) / 4 
if promedio >=6:
    print("felicidades "+nombre + ' "aprobaste "con un promedio de : ',promedio )
    print("disfruta de tus vavaciones ") 
elif promedio < 6 :
    print("esto no termino para ti nos vemos en vacaciones atentamente tu tio ")    