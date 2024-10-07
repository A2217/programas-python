# Crear el diccionario de municipios
municipios = {
    "Apozol": 1863,
    "Calera": 1868,
    "Fresnillo": 1554,
    "Guadalupe": 1821,
    "Jalpa": 1824,
    "Jerez": 1824,
    "Loreto": 1931,
    "Mazapil": 1824,
    "Momax": 1857
}

print("Diccionario de municipios original:")
print(municipios)

del municipios["Apozol"]
print("\nDespués de eliminar Apozol:")
print(municipios)

fresnillo_value = municipios.pop("Fresnillo")
print("\nDespués de eliminar Fresnillo:")
print(municipios)

momax_value = municipios.popitem()
print("\nDespués de eliminar Momax:")
print(municipios)

municipios.clear()
print("\nDespués de borrar todos los elementos:")
print(municipios)
