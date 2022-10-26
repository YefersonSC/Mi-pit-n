#Ejercicio 1:
edad = int(input("Indica tu edad: "))
if edad >= 18:
    print("Usted es mayor de edad.")
else:
    print("Usted es menor de edad.")

#Ejercicio 2:
contraseña = "contraseña"

pregunta = input("\nCuál es la contraseña: ")
if contraseña == pregunta.lower():
    print("La contraseña introducida coincide.")
else:
    print("La contraseña introducida no coicide.")
#En este ejercicio se utilizó la función "lower()"

#Ejercicio 3:
numero1 = float(input("\nIntroduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))
if numero2 == 0 :
    exit("Error")
print("Esta es la división de ambos números:", numero1 / numero2)

#Ejercicio 4:
numero = int(input("\nIntrdouce un número entero: "))
resto = numero % 2
if resto == 0:
    print("Este número es par.")
else:
    print("Este número es impar.")

#Ejercicio 4:
edad = int(input("\nIntroduce tu edad: "))
ingresos = float(input("Introduce tus ingresos mensuales: "))

if edad > 16 and ingresos >= 1000:
    print("Usted debe tributar.")
else:
    print("Usted no tributa.")


