#Dado un cilindro de radio 10.2345 y altura  123.45 
# se desea calcular la circunferencia de la base, área lateral, área de la base, la superficie y el 
# volumen
radio = 10.2345
altura = 123.45 
pi = 3.1416

area_de_la_base = pi * (radio**2)
volumen = area_de_la_base * altura
circunferencia_de_la_base = 2 * pi * radio
area_lateral = 2 * pi * radio * altura 

print("El área de la base es:", area_de_la_base)
print("El volumen es:", volumen)
print("La circunferencia de la base es:", circunferencia_de_la_base)
print("El área lateral es:", area_lateral)