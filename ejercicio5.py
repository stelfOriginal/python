# switch no existe
numero1 = float(input('Insertar numero1->'))
numero2 = float(input('Insertar numero2->'))

eleccion = input('Elige una de las opciones (+, -, *, /)->').lower()
if eleccion == '+':
    suma = numero1 + numero2
    print(suma)
elif eleccion == '-':
    resta = numero1 - numero2
    print(resta)
elif eleccion == '*':
    multi = numero1 * numero2
    print(multi)
elif eleccion == '/':
    divi = numero1 / numero2  
    print(divi)  
else:
    print('Te has equivocado, introduce una de las opciones que hay marcadas')