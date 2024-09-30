#Genera y multiplica listas aleatorias
import random

lista1 = [random.randint(1, 100) for _ in range(10)]
lista2 = [random.randint(1, 100) for _ in range(10)]

lista3 = []

for i in range(10):
    if lista1[i] % 2 != 0 and lista2[i] % 2 != 0: 
        lista3.append(lista1[i] + lista2[i])
    else:
        lista3.append(0)  

print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista 3 (suma de impares):", lista3)
