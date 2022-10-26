print("Programa que solicita tres números enteros y posteriormente el programa determinará e indicará, cuál de los tres números es el más grande.")

numero1 = int(input("Inserte el primer número: "))
numero2 = int(input("Inserte el segundo número: "))
numero3 = int(input("Inserte el tercer número: "))

if numero1 == numero2 == numero3:
    exit("Los tres números no pueden ser iguales")

if numero1 > numero2 and numero1 > numero3:
    print("El núemro más grande es:",numero1)
    exit("Fin del programa")
if numero2 > numero1 and numero2 > numero3:
    print("El número más grande es:",numero2)
    exit("Fin del programa")
if numero3 > numero1 and numero3 > numero2:
    print("El número más grande es:",numero3)
    exit("Fin del programa")