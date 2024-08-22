#p02-area-círculo - calcula el área de un círculo

import math

print("Calculando el area de un círculo : \n")
print("Dame el radio del círcul: ")

radio = float( input() )
#area = 3.1416 * radio * radio 
area = math.pi *radio **2
print(f"\nPara un círculo de radio {radio} el area es {area:.2f}")