# cajero automatico que empieze con 4 mil euros de saldo

# pueden mostrar,ingresar retirar dinero y salir

# saldo = 4000
# ingresar = int(input('Ingresar:-> ' ) )



# switch no existe
numero1 = 4000

eleccion = input('Elige una de las opciones (mostrar, retirar, ingresar, salir)->').lower()
numero2 = float(input('Insertar numero->'))
if eleccion == 'mostrar':
    # mostrar = numero1 + numero2
    print(numero1,'€', 'es tu sueldo')
elif eleccion == 'retirar':
    resta = numero1 - numero2
    print('esto es lo que te queda luego de sacar el dinero', resta,'€')
elif eleccion == 'ingresar':
    suma = numero1 + numero2
    print('este es tu total: ', suma,'€')
elif eleccion == 'salir':
     exit() 
else:
    print('Te has equivocado, introduce una de las opciones que hay marcadas')
