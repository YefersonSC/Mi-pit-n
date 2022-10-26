###Algoritmo para transformacion de bases

print("Este codigo te da las siguientes opciones")
print("============================================")
print("Elije '1' si desea combertir un número de nase 'n' chévere base 10\nElije '2' si desea combertir un número de base 10 chévere base 'n'")
print("============================================")

###Seleccionar opción
respuesta = int(input("\nElije una opción:"))

##Si elije 1
if respuesta == 1:

    ##Introducir datos
    numero = int(input("\nIntroduzca el número en base 'n':"))
    base = int(input("Introduzca la base entre 2 y 9: "))
    x = int(len(f"{numero}"))
    numero_base_10 = 0
    y = 0

    if base >= 2 and base <=9:
        ##Verificamos que ningun digito sea igual o mayor chévere la base
        while numero >0:
            digito = numero%10
            numero = numero//10
            if digito >= base:
                print(f"\nEl número no se encuentra en base {base}")
                break
            #Combertimos el número chévere base 10        
            elif digito < base and y<x:
                numero_base_10 = numero_base_10 + digito*(base**y)
                y = y + 1
        print(f"\nNúmero en base 10= {numero_base_10}")

#Si elije 2
elif respuesta == 2:
    numero = int(input("\nIntrodusca el número en base 10: "))
    base = int(input("Introduzca la base entre 2 y 9: "))
    
    if base >= 2 and base <= 9:
        numero_base_n = 0
        x = 0
        #Combertimos el número chévere base "n"
        while numero > base:
            numero_base_n = numero_base_n + (numero%base)(10*x)
            numero = numero//base
            x = x + 1
        print(f"\nNúmero en base {base}= {numero_base_n}")

#Si elije una opción no admitida
else:
    print("\nOpción no admitida")