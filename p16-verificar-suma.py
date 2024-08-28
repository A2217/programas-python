#Verifica si la suma de dos números es igual a un tercero

import os; os.system("clear")

print("Verifica si la suma de dos números es igual a un tercero")
print("Dame 3 números enteros separados por un enter: ")

n1,n2,n3 = int(input()),int(input()),int(input())

if n1 + n2 == n3:
    print("Son iguales")
else:
    print("Son distintos")

print("\nProceso terminado")