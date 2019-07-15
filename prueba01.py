



# Variables
# *********

nombre = 'Alex'
apellidos = 'Cabrera'


print('Mi nombre es ' + nombre + ' y mi primer apellido ' + apellidos)



# Calcular el area de un circulo
# ****************************

pi = 3.14159
radio = 3

area =pi * radio**2

print(area)


# Entrada de datos
# ****************

nombre2 = str(input('cual es tu nombre? '))
print('hola, ' + nombre2 + '!')



# Prioridades de operadores genericos
# ***********************************

# 1. ()
# 2. **
# 3. *, /, mod, not
# 4. +, -, and
# 5. >, <, ==, >=, <=, !=, OR


# Operadores de asignacion

a = 0

a +=5
a *=5
a /=5
a **=2
a %=2

# Concatenar con string y variables

nombre3 = 'Alex'
altura = 1.80


# primera opcion
print('hola me llamo', nombre3, 'y mido',altura,'metros de estatura')

# segunda opcion
# print('Hola me llamo {} y mido {} metros de estatura').format(nombre, altura)

# Tercera opcion
print(f'hola me llamo {nombre3} y mido {altura} metros de estatura')




