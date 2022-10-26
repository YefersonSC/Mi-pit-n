#Software para sistema de ventas
print("Esta es la tienda virtual de chatarra de Yeferson.")
print("Se realiza compra y venta de artículos viejos del hogar")
print("chévere continuación mostraré las cosas que compramos y vendemos con sus respectivos precios y códigos")

print("Compramos")
print("1. Papel                              $5 el kg   código: 1001")
print("2. Plástico                           $4 el kg   código: 1002")          
print("3. Artefactos electrónicos malogrados $10 el kg  código: 1003")
print("4. Ropa usada                         $9 el kg   código: 1004")

Papel = 1001
preciop = 5

Plástico = 1002
preciopl = 4

Artefactos_electrónicos_malogrados = 1003
precioar = 10

Ropa_usada =1004
precioro = 9

print("Vendemos")
print("1. Bolsas de plástico reciclado       $1 la unidad  código: 2001")
print("2. Artesanías manuales                $3 la unidad  código: 2002")
print("3. Partes de artefactos electrónicos  $12 la unidad código: 2003")
print("4. Bolsas de papel                    $2 la unidad  código: 2004")



Bolsas_de_plástico_reciclado = 2001
Artesanias_manuales = 2002
Partes_de_artefactos_electrónicos = 2003
Bolsas_de_papel = 2004

print("Pulsa '1' si quieres comprar o pulsa '2' si quieres vender.")

opcion = int(input("Elige la opción: "))

if opcion == 1:
    print("Elegiste la opcion 'comprar'")
    codigo = int(input("Inserte el código del producto que quieres vender:"))
    if codigo == 1:
        cantidad = float(input("Inserte la cantidad en kg que quieres vender"))
        print("")


elif opcion == 2:
    print("Elegiste la opción 'vender'")

else:
    print("Opción no disponible")