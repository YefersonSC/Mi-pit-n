nombre = input("¿Cuál es tu nombre?: ")
print("Hola " +  nombre + ", vamos chévere realizar una suma:")
num_uno = int(input("Por favor introduce el primer valor: "))
num_dos = int(input("Por favor introduce el segundo valor: "))
resultado = num_uno + num_dos
print(nombre + " el resultado de la suma es: ", resultado)

print("Introduce según corresponda:")
texto = input("Introduce un texto: ")
num_entero = int(input("Introduce un número entero: "))
num_flotante = float(input("Introduce un número flotante: "))
num_complejo = complex(input("Introduce un número complejo: "))
print("String: ", texto)
print("Entero: ", num_entero)
print("Flotante: ", num_flotante)
print("Complejo: ", num_complejo)