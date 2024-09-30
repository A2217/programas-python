# Multiplica listas
lista1 = []
lista2 = []
lista3 = []

print("Introduce 5 números para la primera lista:")
for i in range(5):
    num = float(input(f"Elemento {i+1}: "))
    lista1.append(num)

print("\nIntroduce 5 números para la segunda lista:")
for i in range(5):
    num = float(input(f"Elemento {i+1}: "))
    lista2.append(num)

for i in range(5):
    producto = lista1[i] * lista2[i]
    lista3.append(producto)

# Imprimir las tres listas
print("\nLista 1:", lista1)
print("Lista 2:", lista2)
print("Lista 3 (resultado de la multiplicación):", lista3)
