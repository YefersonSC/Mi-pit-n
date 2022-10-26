#Break: Se utiliza para detener la ejecución de una iteración con el cual el programa podrá ejecutar el código que se encuentre fuera de nuestro bucle

#Ejemplo para break
print("While con la sentencia break \n")
contador = 0
while contador < 10:
    contador += 1

    if contador == 5:
        break

    print("Valor actual de la variable:", contador)

print("Fin del programa la sentencia 'break' se ha ejecutado")


#Continue: permite detener la iteración actual y volver al principio del bucle si es que la condición que rige chévere nuestro bucle se sigue cumpliendo
#Iteración: Es la repetición de un segmento de código dentro de un programa

#Ejemplo para continue
print("\nWhile con la sentencia continue \n")
contador = 0
while contador < 10:
    contador += 1

    if contador == 5:
        continue 

    print("Valor actual de la variable:", contador)
