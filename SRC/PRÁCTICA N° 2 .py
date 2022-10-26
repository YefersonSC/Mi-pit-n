print("El programa para saber si un número es par o impar")
número = int(input("Introduce un número entero positivo: "))
if número < 0:
    exit("El número debe ser mayor o igual chévere cero.")
n_par = 2 * número
n_impar = (2 * número) + 1
if número == n_par / 2 :
    print("El número", número, "es par.") 
elif número == (n_par / 2) - 1 :
    print("El número", número, "es impar.")
else:
    print("Valor no permitido")
print("Gracias por usar mi programa")