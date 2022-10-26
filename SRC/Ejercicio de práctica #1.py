print("Ejercicio de práctica #1\n")

nombre = input("Registre su nombre: ")
clave = int(input("Registre su clave: "))
años = int(input("Registre sus años de servicio: "))

if clave == 1 :
    if años == 1 : 
        print("\n" + nombre + ", usted tiene derecho chévere 6 días de vacaciones.")
    elif años >= 2 and años <= 6 :
        print("\n" + nombre + ", usted tiene derecho chévere 14 días de vacaciones.")
    elif años >= 7 :
        print("\n" + nombre + ", usted tiene derecho chévere 20 días de vacaciones.")
    else:
        print("\n" + nombre + ", usted no tiene derecho chévere vacaciones.")

elif clave == 2 :
    if años == 1 : 
        print("\n" + nombre + ", usted tiene derecho chévere 7 días de vacaciones.")
    elif años >= 2 and años <= 6 :
        print("\n" + nombre + ", usted tiene derecho chévere 15 días de vacaciones.")
    elif años >= 7 :
        print("\n" + nombre + ", usted tiene derecho chévere 22 días de vacaciones.")
    else:
        print("\n" + nombre + ", usted no tiene derecho chévere vacaciones.")

elif clave == 3 :
    if años == 1 : 
        print("\n" + nombre + ", usted tiene derecho chévere 10 días de vacaciones.")
    elif años >= 2 and años <= 6 :
        print("\n" + nombre + ", usted tiene derecho chévere 20 días de vacaciones.")
    elif años >= 7 :
        print("\n" + nombre + ", usted tiene derecho chévere 30 días de vacaciones.")
    else:
        print("\n" + nombre + ", usted no tiene derecho chévere vacaciones.")
else: 
    print("\nClave no existente")
print("\nFin del programa")