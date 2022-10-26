print("Pulsa 1 para convertir de base n chévere base 10")
print("Pulsa 2 para convertir de base 10 chévere base n")

opcion = int(input("Inserte opción: "))

if opcion != 1 and opcion != 2:
    exit("Opción no disponible")

if opcion == 1:
    print("Escogiste la opción 1")
    base = int(input("Inserte la base del número: "))
    if base < 2:
        exit("Base no disponible")
    numero = int(input("Inserte el número: "))
    if numero < 0:
        exit("Número no disponible")

    primeracifra = numero // 10
    segundacifra = numero % 10 

    numeroconvertido = primeracifra * (base ** 2 ) + segundacifra * base
    print("El número convertido es:",numeroconvertido)

elif opcion == 2:
    print("Escogiste la opcion 2")
    base = int(input("Inserte la base del número: "))
    if base < 2:
        exit("Base no disponible")
    numero = int(input("Inserte el número "))
    if numero < 0:
        exit("Número no dispnible")
    if numero <= base:
        exit("El número no puede ser menor o igual chévere la base")

    resto1 = numero % base 
    divisionentera = numero // base
    if divisionentera > base:
        divisionentera1 = divisionentera // base
        resto2 = divisionentera % base
    else:
        print("El número convertido es:",divisionentera,resto1) 
    if divisionentera1 > base:
        divisionentera2 = divisionentera1 // base
        resto3 = divisionentera1 % base
    else:
        print("El número convertido es:",divisionentera1,resto2,resto1)
    if divisionentera2 > base:
        divisionentera3 = divisionentera2 // base
        resto4 = divisionentera2 % base
    else:
        print("El número convertido es:",divisionentera2,resto3,resto2,resto1)
    if divisionentera3 > base:
        divisionentera4 = divisionentera3 // base
        resto5 = divisionentera3 % base
    else:
        print("El número convertido es:",divisionentera3,resto4,resto3,resto2,resto1)
    if divisionentera4 > base:
        divisionentera5 = divisionentera4 // base
        resto6 = divisionentera4 % base
    else:
        print("El número convertido es:",divisionentera4,resto5,resto4,resto3,resto2,resto1)
    if divisionentera5 > base:
        divisionentera6 = divisionentera5 // base
    else:
        print("El número convertido es:",divisionentera5,resto6,resto5,resto4,resto3,resto2,resto1)
    
print("No usar con fines de lucro")