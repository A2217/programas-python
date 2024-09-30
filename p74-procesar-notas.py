# Procesa notas
notas = []
suma = 0
contador = 0

while True:
    nota = float(input("Introduce una nota (0 para terminar): "))

    if nota == 0:
        break

    if nota < 0 or nota > 100:
        print("Error: la nota debe estar entre 0 y 100.")
    else:
        notas.append(nota)
        suma += nota
        contador += 1

if contador > 0:
    
    promedio = suma / contador

    notas_menores = [n for n in notas if n < promedio]

    print("\nResultados:")
    print(f"Notas introducidas: {notas}")
    print(f"Cantidad de notas: {contador}")
    print(f"Suma de las notas: {suma}")
    print(f"Promedio de las notas: {promedio:.2f}")
    print(f"Notas menores al promedio: {notas_menores} ({len(notas_menores)})")
    print(f"Nota máxima: {max(notas)}")
    print(f"Nota mínima: {min(notas)}")
else:
    print("No se han introducido notas válidas.")
