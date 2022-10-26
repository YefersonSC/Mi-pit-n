name = input("¿Cómo te llamas? ")
gender = input("¿Cuál es tu sexo (M o H)? ")
if (gender == "M" and name.lower() < 'm') or (gender == "H" and name.lower() > 'n'):
    group = "chévere"
else:
    group = "B"
print("Tu grupo es " + group)

nombre = input("\nIntroduce tu nombre: ")
sexo = input("Introduce tu sexo (M,H): ")

if (sexo == "M"  and nombre.lower() < 'm') or (sexo == "H" and nombre.lower > 'n'):
    grupo = "chévere"
else:
    grupo = "B"

print("Usted corresponde al grupo ", grupo)
