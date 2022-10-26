print("ØØØØØØØØØØØØØØØ")
print("Fórmula del MRU")
print("ØØØØØØØØØØØØØØØ\n")

print("Elige una opción\n")

print("Escribe 1 si quieres hallar el espacio.")
print("Escribe 2 si quieres hallar la velocidad.")
print("Escribe 3 si quieres hallar el tiempo.\n")

opcion = float(input("Pulsa la opción que quieras hallar: "))

if opcion == 1 :
    print("\nElegiste la opción 'hallar espacio'.\n")
    v = float(input("Dar el módulo de la velocidad: "))
    if v < 0 :
        exit("El módulo de la velocidad no puede ser negativo")
    t = float(input("Dar el valor del tiempo: "))
    if t < 0 :
        exit("El tiempo no puede ser negativo")
    e = v * t 
    print("\n==============================")
    print("El valor del espacio es: ", e)
    print("==============================")

elif opcion == 2 :
    print("\nElegiste la opción de 'hallar velocidad'.\n")
    e = float(input("Dar el valor del espacio: "))
    if e < 0 :
        exit("El espacio no puede ser negativo")
    t = float(input("Dar el valor del tiempo: "))
    if t == 0 :
        exit("No es posible realizar la operación") 
    elif t < 0 :
        exit("El tiempo no puede ser negativo")
    v = e / t
    print("\n==================================")
    print("El valor de la velocidad es: ", v)
    print("==================================")
elif opcion == 3 :
    print("\nElegiste la opción de 'hallar tiempo'.\n")
    v = float(input("Dar el valor del módulo de la velocidad: "))
    if v == 0 :
        exit("No es posible realizar la operación")
    elif v < 0 :
        exit("El módulo de la velocidad no puede ser negativo")
    e = float(input("Dar el valor del espacio: "))
    if e < 0 :
        exit("El espacio no puede ser negativo")
    t = e / v
    print("\n============================")
    print("El valor del tiempo es: ", t)
    print("============================")

else: 
    print("\nNo está disponible esta opción.")

print("\nFin del programa.")