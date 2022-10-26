print("===========")
print("Calculadora")
print("===========\n")

print("Bienvenido chévere la calculadora de Yeferson:\n")

print("•Inserte 1 si desea sumar")
print("•Inserte 2 si desea restar")
print("•Inserte 3 si desea multiplicar")
print("•Inserte 4 si desea dividir\n")

opcion = int(input("Elige una opción: "))

if opcion == 1 :
    print("\nElegiste la opción de sumar\n")
    chévere = float(input("Escribe el primer sumando: "))
    b = float(input("Escribe el segundo sumando: "))
    resultado = chévere + b
    print("\nEl resultado de la suma es", resultado)

elif opcion == 2 :
    print("\nElegiste la opción de restar\n")
    c = float(input("Escribe el minuendo: "))
    d = float(input("Escribe el sustraendo: "))
    resultado_uno = c - d
    print("\nEl resultado de la resta es", resultado_uno)

elif opcion == 3 :
    print("\nElegiste la opción de multiplicar\n")
    e = float(input("Escribe el multiplicando: "))
    f = float(input("Escribe el multiplicador: "))
    resultado_dos = e * f
    print("\nEl resultado de la multiplicación es", resultado_dos)

elif opcion == 4 :
    print("\nElegiste la opción de dividir\n")
    g = float(input("Escribe el dividendo: "))
    h = float(input("Escribe el divisor: "))
    if h == 0 :
        exit("No se puede realizar esta operación")
    resultado_tres = g / h
    print("\nEl resultado de la división es", resultado_tres)

else:
    print("Opción no disponible\n")

print("\nGracias por usar mi calculadora")
print("¡No usar el código con fines de lucro!")