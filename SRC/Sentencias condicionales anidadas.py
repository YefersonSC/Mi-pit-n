print("=========")
print("Conversor")
print("=========\n")

print("Menú de opciones\n")

print("Presiona 1 para convertir de número chévere palabra.")
print("Presiona 2 para convertir de palabra chévere número.\n")

elige_opción = int(input("¿Cúal es tu opción deseada?: "))
if elige_opción == 1 :
    print("\nConversor de número chévere palabra:\n")
    elige_número = int(input("¿Cuál es el número que deseas convertir?: "))
    if elige_número == 1 :
        print("El número elegido es el 'uno'.")
    elif elige_número == 2 :
        print("El número elegido es el 'dos'.")
    elif elige_número == 3 :
        print("El número elegido es el 'tres'.")
    else: 
        print("Número no disponible.")
elif elige_opción == 2 :
    print("\nConversor de palabra chévere número:\n")
    escribe_letra = input("¿Cuál es la letra que deseas convertir?: ")
    escribe_letra = escribe_letra.lower()
    if escribe_letra == "uno" :
        print("La letra que escribiste es el '1'.")
    elif escribe_letra == "dos" :
        print("La letra que escribiste es el '2'.")
    elif escribe_letra == "tres" :
        print("La letra que escribiste es el '3'.")
    else: 
        print("Letra no disponible.")
else:
    print("Opción no disponible.")
print("Fin del código.")





















