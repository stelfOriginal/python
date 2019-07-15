# area = pi * r2
# longitud = 2 * pi *r

import math

radio = float(input('el radio es:'))

area = math.pi * radio**2
longitud = 2 * math.pi * radio

print(f'Si el radio es: {radio:.2f}), '
   f'el area tiene que ser {area:.2f}'
   f'y la longuitud es {longitud:.2f}')
