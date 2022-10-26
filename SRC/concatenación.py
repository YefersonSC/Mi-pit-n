#Número 1:
nombre = "Carlos"
edad = 22

print("Hola {} tienes {} años.".format(nombre, edad))

#Método 2:
nombre =input("Nombre: ")
edad = int(input("Edad: "))

print("Hola {} tienes {} años.".format(nombre, edad))

#Método 3:
print("Hola {nombre} tienes {edad} años.".format(nombre = "Yeferson", edad = 18))

#Método 4:
print("Hola {nombre} tienes {edad} años.".format(nombre = input("Nombre: "), edad = int(input("Edad: "))))

#Método 5:
nombre = "Yeferson"
edad = 18
print("Hola {0} tienes {1} años.".format(nombre, edad))

#Método 6:
nombre = input("Nombre: ")
edad = int(input("Edad: "))
print("Hola {0} tiene {1} años.".format(nombre, edad))