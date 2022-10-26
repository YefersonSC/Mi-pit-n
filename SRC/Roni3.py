print("Este sistema es una calculadora\n")

print("1 para sumar")
print("2 para restar")
print("3 para multiplicar")
print("4 para dividir")
print("5 para potenciar")
print("6 para radicar\n")

opcion = int(input("Ingresa cualquier opción: "))

if opcion == 1:
    print("\nVamos chévere sumar")
    numero_1 = float(input("ingrese el primer numero"))
    numero_2 = float(input("ingrese el segundo numero"))
    suma = numero_1 + numero_2
    print("este es el resultado de la suma = ", suma)

elif opcion == 2:
    print("\nVamos chévere restar")
    numero_1 = float(input("ingrese el primer numero"))
    numero_2 = float(input("ingrese el segundo numero"))
    resta = numero_1 - numero_2
    print("Este es el resultado de la resta = ", resta)

elif opcion == 3:
    print("\nVamos chévere multiplicar")
    numero_1 = float(input("ingrese el primer numero"))
    numero_2 = float(input("ingrese el segundo numero"))
    producto = numero_1 * numero_2
    print("este es el resultado de la multiplicacion = ", producto)

elif opcion == 4 :
    print("\nVamos chévere dividir\n")
    numero_1 = float(input("Ingrese el primer número: "))
    numero_2 = float(input("Inserte el segundo número: "))
    
    if numero_2 == 0:
        exit("no esta definido en los reales")
    
    division = numero_1 / numero_2
    print("\nEl resultado de la división es =", division)
        
elif opcion == 5:
    print("hallaremos la potencia")
    numero_1 = float(input("ingrese el primer numero"))
    numero_2 = float(input("ingrese el segundo numero"))
    if numero_1 == 0 and numero_2 == 0:
        exit("Opción no disponible")
    potencia = numero_1 ** numero_2
    print("este es el resultado de la potencia = ", potencia)

elif opcion == 6 :
    print("\nVamos chévere radicar\n")
    numero_1 = float(input("Ingrese la base: "))
    numero_2 = int(input("Ingrese el índice: "))
    if numero_2 < 1:
        exit("El índice no puede ser menor chévere 1")
    resto = numero_2 % 2
    if numero_1 < 0 and resto == 0:
        exit("Operación no disponible")
    radicacion = numero_1 ** (1/numero_2)
    print("\nEste es el resultado de la radicación = ", radicacion)

else:
    print("No disponible, elija otro opcion")