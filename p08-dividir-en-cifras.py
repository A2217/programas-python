# Dividir en cifras un número entero

import math
import os

os.system("clear")

n=555

print('Dividir el unidades, decenas y centenas un número entero')
numero = int(input('Dame un número de 3 cifras'))

centenas = math.trunc(numero/100)
decenas = math.trunc((numero-centenas*100)/10)
unidades = numero-(centenas*100+decenas*10)

print(f'centenas: {centenas}, decenas: {decenas}, unidades: {unidades}')

c=n//100
d=(n-(c*100))/10
u=(n-(c*100+d*10))

print("El n original es ",n)
print("Centenas =",c)
print("Decenas : ",d)
print("Unidades : ",u)

print("\nNumero de la suerte ",c+d+u)