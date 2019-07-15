# a = 5
# ​
# if a > 10:
#     print('Esrto es un if')
# elif 10 == 0:
#     print('Esto es un elif')
# else:
#     print('Esto es un else')


    # IF, anidado

edad = int(input('Cual es tu edad: '))
if edad >= 0 and edad < 120:
    print('la introduccion de datos es correcta')
    if edad >= 18:
        print('Eres mayor de edad')
    if edad < 18:
        print('eres un pitufo')
else:
        print('te has equivocado con la introduccion de la edad so cani')