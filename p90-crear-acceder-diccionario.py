# Crear el diccionario de días
dias = {
    1: "Lunes",
    2: "Martes",
    3: "Miércoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sábado",
    7: "Domingo"
}

print("Diccionario de días:")
print(dias)

print("\nPrimer elemento: ")
print(dias[1])

print("\nÚltimo elemento: ")
print(dias[7])

print("\nQuinto elemento: ")
print(dias.get(5))

print("\nSéptimo elemento: ")
print(dias.get(7))

print("\nDiccionario completo:")
for key, value in dias.items():
    print(f"{key}: {value}")
