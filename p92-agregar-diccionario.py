# Crear el diccionario de ventas
ventas = {
    "Juan": 1550,
    "Jose": 2600,
    "Maria": 2220
}

print("Diccionario de ventas original:")
print(ventas)

ventas["Rocio"] = 2500

ventas["Mateo"] = 1567

ventas.update({"Andrea": 9567})

ventas.update({"Miguel": 1234})

print("\nDiccionario de ventas actualizado:")
for key, value in ventas.items():
    print(f"{key}: {value}")
