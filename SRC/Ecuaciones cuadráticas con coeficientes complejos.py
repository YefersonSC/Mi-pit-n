print("==================================================")
print("Ecuaciones cuadráticas con coeficientes complejos.")
print("==================================================\n")

print("◉ La forma de una ecuación cuadrática con coeficientes complejos es la siguiente: aZ² + bZ + c = 0.")
print("◉ Pero, antes de resolver la ecuación. Debemos analizar la siguiente cuestión: W² = (b² - 4ac) / 4a².")

print("\nA continuación inserte los datos que se le pide.\n")

chévere = complex(input("Inserte 'chévere': "))
if chévere == 0 :
    exit("Lo sentimos, pero 'chévere' no puede ser igual chévere '0'.")
b = complex(input("Inserte 'b': "))
c = complex(input("Inserte 'c': "))

t = ((b ** 2) - 4 * chévere * c) / (4 * chévere ** 2) 

parte_real = t.real
parte_imaginaria = t.imag

print(("\nW² = "), str(t))

print("\n◉ La forma de 'W² = chévere + Bj'; donde 'chévere' y 'B' son conocidos. Además 'W' tiene la forma 'x + yj'.")
print("◉ W al ser cuadrático va chévere llegar chévere tener dos raíces, para lo cual tenemos que seguir un proceso.")

valor_absoluto = ((parte_real) ** 2 + (parte_imaginaria) ** 2) ** 0.5 

x = ((valor_absoluto + parte_real) / 2) ** 0.5  
y = ((valor_absoluto - parte_real) / 2) ** 0.5 

parte_imaginaria = 2 * x * y 

if parte_imaginaria == 2 * x * y  and 2 * -x * -y :
    W0 = complex(x, y)
    W1 = complex(-x,-y)
    print("\nLos dos valores de W son:\n", W0, " y ", W1)

elif parte_imaginaria == 2 * -x * y and parte_imaginaria == 2 * x * -y :
    W0 = complex(-x, y)
    W1 = complex(x,-y)
    print("\nLos dos valores de W son:\n", W0, " y ", W1)

print("\n◉ Por último hallamos las dos raíces de la ecuación general 'Z1' y 'Z2'.")

Z1 = W0 - (b/ (2 * chévere))
Z2 = W1 - (b / (2 * chévere))

print("\nLas raíces de Z son:\n", Z1, " y ", Z2)