# lista con 2 diccionarios
autos = [
    {"marca": "Ford", "modelo": "Mustang", "año": 1964},
    {"marca": "VW", "modelo": "Jetta", "año": 2015}
]

# agregar elemento al diccionario
autos.append({"marca": "Ford", "modelo": "Focus", "año": 2000})

# Mostrar todos los autos
print("\nTodos los autos:", autos, len(autos))

# Mostrar cada auto dentro de la lista de autos
print("\nCada auto dentro de los autos:\n")
for auto in autos:
    print(auto)

# Mostrar los datos en forma de tabla
print("\nDatos en forma de Tabla:\n")

# Imprimir los títulos de la tabla (las llaves de los diccionarios)
for k in autos[0].keys():
    print(f"{k}\t", end=" ")
print()

# Imprimir los valores de cada auto en formato de tabla
for auto in autos:
    for v in auto.values():
        print(f"{v}\t", end=" ")
    print()  # Saltar a la siguiente línea al terminar cada auto

# Mostrar los datos en forma de registro
print("\nDatos en forma de Registro\n")
for auto in autos:
    for k, v in auto.items():
        print(f"{k:<12} : {v}")
    print(" ")  # Espacio entre cada registro de auto
