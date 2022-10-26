print("Cadena de caracteres")
mensaje = "Hola Yeferson"
mensaje += " ¿Cómo estás?"
print(mensaje)

print("Concatenación:")
mensaje = "Hola"
nombre = " Yeferson"
pregunta = " ¿Cómo estás?"
print(mensaje + nombre + pregunta)

numero_uno = 4
numero_dos = 6
resultado = numero_uno + numero_uno
print("El resultado de la suma es: " + str(resultado))

print("Búsqueda:")
mensaje = "Hola Yeferson"
buscar_subcadena = mensaje.find("Yeferson")
print(buscar_subcadena)

print("Extracción:")
mensaje = "Hola Yeferson"
extraer_subcadena = mensaje[1:8]
print(extraer_subcadena)

print("Comparación:")
mensaje_uno = "Hola"
mensaje_dos = "Hola"
print(mensaje_uno == mensaje_dos) 