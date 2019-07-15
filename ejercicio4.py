# Calcula cual es mayor de las 3 personas y te dice cuantos años le saca a las otras 2 personas
nombre1 = str(input('Introduce el nombre del primer conejillo de indias y su edad. Nombre->'))
edad1 = int(input('Edad :-> '))
nombre2 = str(input('Introduce el nombre del segundo conejillo de indias y su edad. Nombre->'))
edad2 = int(input('Edad:-> '))
nombre3 = str(input('Introduce el nombre del tercero conejillo de indias y su edad. Nombre->'))
edad3 = int(input('Edad 3:-> '))
if edad1 > edad2 and edad3:
    calculo = edad1 - edad2
    calculo2 = edad1 - edad3
    print(f'{nombre1} con {edad1} es mayor y le saca {calculo} a {nombre2} y {calculo2} a {nombre3}')
elif edad2 > edad3 and edad1:
    calculo = edad2 - edad3 
    calculo2 = edad2 - edad1
    print(f'{nombre2} con {edad2} es mayor y le saca {calculo} a {nombre3} y {calculo2} a {nombre1}')
elif edad3 > edad2 and edad1:
    calculo = edad3 - edad1
    calculo2 = edad3 - edad2
    print(f'{nombre3} con {edad3} es mayor y le saca {calculo} a {nombre1} y {calculo2} a {nombre2}')











