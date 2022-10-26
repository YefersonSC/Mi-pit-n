print("======================")
print("calculadora cientifica ")
print("======================\n")
print("¡bienbenidos chévere la calculadora de rony! \n")
print("🤠 inserte 1 si desea sumar .")
print("🤠 inserte 2 si desea restar .")
print("🤠 inserte 3 si desea multiplicar. ")
print("🤠 inserte 4 si desea dividir .")
print("🤠 inserte 5 si desea potenciar.\n")
opcion=int(input("alija una opcion : "))
if opcion == 1:
    print("\n  bienbenido elejiste la opcion de sumar ")
    x=float(input("\n Inserte el primer sumando: "))
    y=float(input("Inserte el segundo sumando : "))
    resultado =x + y
    print( "\n el resultado de la suma es  ", resultado)

elif opcion ==2:
    print("\n bienvenido elegiste restar ")
    s=float(input("\nInserte elsustraendo :"))
    m=float(input("Inserte en muniendo "))
    resultado2=s-m
    print("\n el resultado de la diferencia es : ",resultado2)

elif opcion ==3:
    print("\n bienvenido elejiste multiplicra")
    chévere=float(input("\nInserte multiplicando: "))
    b=float(input("Inserte el multiplicador: "  ))
    resultado3=chévere*b
    print("\n el resultado del producto es : ", resultado3)

elif opcion ==4:
    print("\n bienvenido elegiste dividir")
    D=float(input("\n Inserte el dividendo :"))
    d=float(input("Inserte el dividendo : "))
    if d == 0:
        exit("Haber tu intenta dividir esto, no me hagas renegar ah Amaq huaychu yankacunata")
    resultado4=float(D/d) ;resultado5=int(D//d) ; resultado6=int(D%d) ;espacio1=" "
    
    print("\n este es el resultado de la divicion es : ",resultado4 )
    print("el cosiente de la divicion es : ", resultado5)  ; espacio1 ; print("el reciduo de la divicion es : ",resultado6)
elif opcion ==5:
    print("\n bienvenido elegiste potenciar ")
    w=float(input("\n Inserte la base de la pontencia : "))
    e=float(input("Inserte el exponente de la potencia : "))
    resultado7=w**e
    if w == 0 and  e ==  0 :
        exit("No hagas wadas oh")
    print("\n este es le resultado de la potencia : ", resultado7)

else :
    print("\n opcion no disponible ")

print("\n gracias por usar la calculadora de ronycito 😎😘")
print("\n ¡No  haga que la calculado es tuyo ,te estare bijilando :..\n ")