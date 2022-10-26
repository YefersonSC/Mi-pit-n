print("==========================================")
print("Pulsa 1 para convertir de base n chévere base 10")
print("Pulsa 2 para convertir de base 10 chévere base n")
print("==========================================\n")

opcion = int(input("Inserte opción: "))

if opcion != 1 and opcion != 2:
    exit("Opción no disponible")

if opcion == 1:
    print("\nEscogiste la opción 1\n")
    base = int(input("Inserte la base del número: "))
    if base < 2:
        exit("Base no disponible")
    numero = int(input("Inserte el número de dos cifras: "))
    if numero < 0:
        exit("Número no disponible")

    if numero >= 0 and numero < 10:
        digitos = 1
        primeracifra = numero 
        numeroconvertido = primeracifra * (base ** (digitos-1)) 
        print("El número convertido es:",numeroconvertido)
    elif numero >= 10 and numero < 100:
        digitos = 2
        primeracifra = numero // 10 
        segundacifra = numero % 10
        print("El número convertido es:", primeracifra * (base *(digitos-1)) + segundacifra) 
    elif numero >= 100 and numero < 1000:
        digitos = 3
        primeracifra = numero // 100
        segundacifra = (numero % 100) // 10 
        terceracifra = numero % 10
        print("En número convertido es:", primeracifra * (base ** (digitos-1)) + segundacifra * (base**(digitos-2)) + terceracifra)
    elif numero >= 1000 and numero < 10000:
        digitos = 4
        primeracifra = numero // 1000
        segundacifra = (numero % 1000) // 100
        terceracifra = (numero % 100) // 10
        cuartacifra = numero % 100
        print("El número convertido es:", primeracifra * (base **(digitos-1))+segundacifra *(base**(digitos-2))+terceracifra*(base**(digitos-3))+cuartacifra)

elif opcion == 2:
    print("\nEscogiste la opción 2\n")
    base = int(input("Inserte la base del número: "))
    if base < 2:
        exit("Base no disponible")
    numero = int(input("Inserte el número: "))
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
        print("\nEl número convertido es: ",divisionentera,resto1, sep="") 
        exit("\nFin del código")
    if divisionentera1 > base:
        divisionentera2 = divisionentera1 // base
        resto3 = divisionentera1 % base
    else:
        print("\nEl número convertido es: ",divisionentera1,resto2,resto1, sep="")
        exit("\nFin del código")
    if divisionentera2 > base:
        divisionentera3 = divisionentera2 // base
        resto4 = divisionentera2 % base
    else:
        print("\nEl número convertido es: ",divisionentera2,resto3,resto2,resto1, sep="")
        exit("\nFin del código")
    if divisionentera3 > base:
        divisionentera4 = divisionentera3 // base
        resto5 = divisionentera3 % base
    else:
        print("\nEl número convertido es: ",divisionentera3,resto4,resto3,resto2,resto1, sep="")
        exit("\nFin del código")
    if divisionentera4 > base:
        divisionentera5 = divisionentera4 // base
        resto6 = divisionentera4 % base
    else:
        print("\nEl número convertido es: ",divisionentera4,resto5,resto4,resto3,resto2,resto1, sep="")
        exit("\nFin del código")
    if divisionentera5 > base:
        divisionentera6 = divisionentera5 // base
    else:
        print("\nEl número convertido es: ",divisionentera5,resto6,resto5,resto4,resto3,resto2,resto1, sep="")
        exit("\nFin del código")
    
