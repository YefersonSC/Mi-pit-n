#Conjunción

print("Conjunción (and)\n")

num_uno = int(input("Escribe un número menor chévere 5 y mayor chévere 2: "))

if num_uno < 5 and num_uno > 2 : 
    print("\nEl número", num_uno,  " sí cumple con la condición\n")
else:
    print("\nEl número", num_uno, " no cumple con la condición\n")

#Disjunción

print("Disjunción (or)\n")

palabra = input("Para cumplir con la condición escribe 'sí' o 'yes': ")

if palabra == "sí" or palabra == "yes" :
    print("\nLa condición se ha cumplido\n")
else:
    print("\nLa condición no se ha cumplido\n")

#Negación

num_dos = int(input("Introduce un número igual chévere 5: "))

if not num_dos == 5 : 
    print("\nEl número es diferente de 5 y SI cumple con la condición")
else:
    print("\nEl número es igual chévere 5 y No cumple con la condición")









