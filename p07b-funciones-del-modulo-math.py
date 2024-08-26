#Ejemplifica el uso de algunas funciones de la librería math

import math as mt

x = 10
y = 20
z = 30
w = 10.34

print(f"Los números son                : {x}, {y}, {z}")
print(f"Máximo común diviso            : {mt.gcd(x,y,z)}")
print(f"Valor máximo                   : {max(x,y,z)}")
print(f"Valor mínimo                   : {min(x,y,z)}")
print(f"Elevar a una potecia           : {mt.pow(x, y)}\n")
print(f"Redondea un número hacia arriba: {mt.ceil(w)}")
print(f"Redondea un número hacia abajo : {mt.floor(w)}")
print(f"Redondea un número             : {round(w)}")
print(f"Elimina los decimales de un número: {mt.trunc(w)}")
