#Ejercicio 5:
renta = float(input("Inserte la renta que percibe: "))

if renta < 10000:
    tipo = 5/100
elif 10000 <= renta < 20000:
    tipo = 15/100
elif 20000 <= renta < 35000:
    tipo = 20/100
elif 35000 <= renta < 60000:
    tipo = 30/100
elif renta > 60000:
    tipo = 45/100

print("El tipo impositivo que le corresponde es", renta * tipo, "$.")

#Ejercico 6:
puntuacion_del_usuario = float(input("\nInserte su puntuación: "))
if puntuacion_del_usuario == 0.0:
    dinero_conseguido = puntuacion_del_usuario * 2400
    rendimiento = "inaceptable"
elif puntuacion_del_usuario == 0.4:
    dinero_conseguido = puntuacion_del_usuario * 2400
    rendimiento = "aceptable"
elif puntuacion_del_usuario > 0.6:
    dinero_conseguido = puntuacion_del_usuario * 2400
    rendimiento = "meritorio"
else:
    print("Inserte una puntuación válida: ")

print("El nivel de rendimiento de usted es", rendimiento, "y el dinero que recibirá será de", dinero_conseguido, "$")

#Ejercico 7:
edad = int(input("\n¿Cuál es tu edad? "))

if edad < 4:
    precio = 0
elif 4 <= edad < 18:
    precio = 5
elif edad >= 18:
    precio = 10

print("El precio que debe pagar para ingresar es $", precio, sep = "")

#Ejercico 8:
pizza = input("\n¿Quiéres una pizza vegetariana, si o no?: ")

if pizza.lower() == "si":
    print("Los ingredientes de tu pizza son: pimiento y tofu.")
elif pizza.lower() == "no":
    print("Los ingredientes de tu pizza son: peperoni, jamón y salmón.")
else:
    print("Respuesta no aceptada.")

