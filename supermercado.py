# mayor de 50=15 de descuento
# menor de 30= si llegas a 50 euro tendras 15% de descuento



# # switch no existe
# patata =4
# hamburgesa = 20
# helado = 8

# patata = float(input('Insertar patata:'))
# hamburgesa = float(input('Insertar hamburgesa:'))
# helado = float(input('Insertar helado:'))


# eleccion = input('Elige una de las opciones (+)->').lower()
# if eleccion == '+':
#     suma = patata + hamburgesa + helado
#     print(suma)
# else:
#     print('Te has equivocado, introduce una de las opciones que hay marcadas')

# *****************************************************************************************************************************************

producto01 = input('Producto:')
precio = float(input(f'Precio del {producto01}:'))
producto02 = input('Producto:')
precio += float(input(f'Precio del {producto02}:'))
producto03 = input('Producto:')
precio += float(input(f'Precio del {producto03}:'))
 

print(f'Total de la compra: {precio:.2f}€')


if precio>50:
    print('Has conseguido un descuento del 15%')
    precioOficial = precio * (85/100)

    print(f'Precio con el descuento del 15% =', precioOficial)
elif precio<30:
    print('Tienes que concederme tu codigo postal,puto,asi te dare un descuento del 10%')
    postal = input('Codigo Postal:')
    precioOficial2 = precio * (90/100)
    iva = precio * 0.21
    print(f'IVA =',iva)
    print(f'Descuento =',precioOficial2)
    print(f'Total% =', precioOficial2 + iva )