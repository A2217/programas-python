# Ista de impares

n = int(input("¿Cuántos números impares deseas generar?: "))

impares = []

for i in range(1, 2*n, 2):
    impares.append(i)

print(f"\nLista de los primeros {n} números impares: {impares}")

suma_impares = sum(impares)
promedio_impares = suma_impares / len(impares)
print(f"\nSuma de los números impares: {suma_impares}")
print(f"Promedio de los números impares: {promedio_impares}")

divisibles_por_3 = [num for num in impares if num % 3 == 0]
suma_divisibles_3 = sum(divisibles_por_3)
print(f"\nNúmeros divisibles entre 3: {divisibles_por_3}")
print(f"Suma de los números divisibles entre 3: {suma_divisibles_3}")

elemento_a_buscar = int(input("\nIntroduce un número para buscar en la lista: "))

if elemento_a_buscar in impares:
    posicion = impares.index(elemento_a_buscar)+1
    print(f"El número {elemento_a_buscar} está en la lista en la posición {posicion}.")
else:
    print(f"El número {elemento_a_buscar} no está en la lista.")
