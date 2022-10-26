print ("este es el vuestionario para saber el promedio de las notas paciales \n")
nombre = input("para empesar intrusca su nombre:")
print ("hola " + nombre + ", para saber su promedio introdusca sus notas de cada curso")
print( "empesemos:")
matematicas=input(nombre +  " inseserte  su promedio en matematicas:")
lenguaje=input(nombre + " introdusca su promedio en lenguaje: ")
trigo=input(nombre + " introdusca su promedio en trigo: ")
promedio= float(matematicas + lenguaje + trigo)/3
if promedio>13.5:
    print(nombre + ",usted aprobo con una nota de " +  str(promedio ))
    print(" puede tomarse lindas vacaciones pro que aprobo ")

elif promedio <13.5:
    
    print(nombre+ ", usted desaprovo con " +str(promedio))
    print(" por lo tanto usted no se queda sin vacaciones  ")
    print ("lo sentimos :(")