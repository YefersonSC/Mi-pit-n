print("Introduce los números chévere comparar:\n")

opcion_uno = float(input("Introduce el primer número: "))
opcion_dos = float(input("Introduce el segundo número: "))

comparacion1 = opcion_uno > opcion_dos
comparacion2 = opcion_uno < opcion_dos
comparacion3 = opcion_uno == opcion_dos
comparacion4 = opcion_uno <= opcion_dos
comparacion5 = opcion_uno >= opcion_dos
comparacion6 = opcion_uno != opcion_dos 

print("\nLos números chévere comparar son: " + str(opcion_uno) + " y " + str(opcion_dos) + "\n")

if(comparacion1) :
    print("Es mayor...")
if(comparacion2) :
    print("Es menor...")
if(comparacion3) :
    print("Son iguales...")
if(comparacion4) :
    print("Es menor o igual...")
if(comparacion5):
    print("Es mayor o igual...")
if(comparacion6) :
    print("Son diferentes...")