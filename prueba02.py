# Entrada de datos

# input te guarda datos tipo cadena 
nombre = input(' tu nombre:')

# input guardar valores numericos
edad = int(input('tu edad: '))
altura = float(input('tu altura:'))

print(f'Hola  {nombre}, y tu edad es {edad}, como tu altura {altura}')

#funciones integradas 
n = int('10')

print(n)

# convertir un string en decimal
n = float('10.4')
print(n)

# convertir un numero a una string
n = str(10)
print(n)

# convertir un numero a binario
n = bin(10)
print(n)

# convertir un numero a hexadecimal
n = hex(10)
print(n)

# convertir un binario a entero
n = int('0b1010', 2)
print(n)

# convertir un hexadecimal a entero
n = int('0xa', 16)
print(n)

# convertir un negativo en positivo
n = abs(-12)

# convertir de numero decimal a entero 
n = round(4.8)
print(n)

# cuenta cantidad de caracteres
n = len('Alex')
print(n)
