print("Calculadora con una sola variable\n")

print("********************")
print("* Menú de opciones *")
print("********************\n")

print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. División entera")
print("6. Exponente")
print("7. Módulo o resto\n")

opcion = int(input("Introduce la opción deseada: "))

if opcion == 1:
    print("Elegiste suma\n")
    numero = float(input("Intoduce el primer número: "))
    numero += float(input("Introduce el segundo número: "))
    print("El resultado de la suma es:",numero)
elif opcion == 2:
    print("Elegiste resta\n")
    numero = float(input("Intoduce el primer número: "))
    numero -= float(input("Introduce el segundo número: "))
    print("El resultado de la resta es:",numero)
elif opcion == 3:
    print("Elegiste multiplicación\n")
    numero = float(input("Intoduce el primer número: "))
    numero *= float(input("Introduce el segundo número: "))
    print("El resultado de la multiplicación es:",numero)
elif opcion == 4:
    print("Elegiste división\n")
    numero = float(input("Intoduce el primer número: "))
    numero /= float(input("Introduce el segundo número: "))
    print("El resultado de la división es:",numero)
elif opcion == 5:
    print("Elegiste división entera\n")
    numero = float(input("Intoduce el primer número: "))
    numero //= float(input("Introduce el segundo número: "))
    print("El resultado de la división entera es:",numero)
elif opcion == 6:
    print("Elegiste exponente\n")
    numero = float(input("Intoduce el primer número: "))
    numero **= float(input("Introduce el segundo número: "))
    print("El resultado del exponente es:",numero)
elif opcion == 7:
    print("Elegiste módulo o resto\n")
    numero = float(input("Intoduce el primer número: "))
    numero %= float(input("Introduce el segundo número: "))
    print("El resultado del módulo o resto es:",numero)
else:
    print("Opción no disponible")

