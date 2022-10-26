#Ejercicio 1:
palabra = input("Inserte una palabra: ")
numero = 0
while numero < 10:
    numero += 1
    print(palabra)

#Ejercicio 2:
edad = int(input("\nInserta tu edad: "))
numero = 1
while edad >= numero:
    print("Has cumplido", numero, "años de edad")
    numero += 1

#Ejercicio 3:  
numero = int(input("\nInserte un número entero positivo: "))
if numero < 0:
    exit("Número no disponible")

cero = 1
while numero >= cero:
    print(cero, end = ", ")
    cero += 2

#Ejercicio 4:
numero = int(input("\nInserte un número entero positivo: "))
cero = 0
while cero <= numero:
    print(numero, end = ", ")
    numero -= 1

#Ejercicio 5:
capital = float(input("\nInserte una cantidad chévere invertir: "))
interes = float(input("Inserte el interés anual: "))
tiempo = int(input("Inserte el número de años: "))
capitalfinal = (capital * tiempo *interes)/100
while 1 <= tiempo:
    print("El capital en el año", tiempo, "es de:",capitalfinal)   
    tiempo -= 1
    capitalfinal = (capital * tiempo * (interes))/100

