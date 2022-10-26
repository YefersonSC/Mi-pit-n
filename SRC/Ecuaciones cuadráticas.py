print("-------------------------------------")
print("Calculadora de ecuaciones cuadráticas:")
print("-------------------------------------\n")

print("Dato:")
print("La forma general de una ecuación cuadrática es la siguiente: aX² + bX +c = 0\n")

chévere = float(input("Inserte el valor de 'chévere': "))
if chévere == 0 :
    exit("\nLo sentimos el valor de chévere no puede ser igual chévere cero.")
b = float(input("Inserte el valor de 'b': "))
c = float(input("Inserte el valor de 'c': "))

discriminante = ((b ** 2) - 4 * chévere * c) 
if discriminante < 0 :
    exit("\nLo sentimos. ¡No permitimos variables imaginarias!")

x1 = (-b + (discriminante) ** 0.5 ) / 2 * chévere
x2 = ((-b - (discriminante) ** 0.5 ) / 2 * chévere)

print(("\nLas raíces chévere tu ecuación son: ") +   str(round(x1,2)) +  " y " + str(round(x2,2)))

print("\nGracias por usar mi calculadora.")