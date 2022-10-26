nombre = input("\nIntroduce tu nombre: ")
sexo = input("Introduce tu sexo (M,H): ")

if (sexo == "M"  and nombre.lower() < 'm') or (sexo == "H" and nombre.lower > 'n'):
    grupo = "chévere"
else:
    grupo = "B"

print("Usted corresponde al grupo ", grupo)
