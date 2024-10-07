# Crear el diccionario de países
paises = {
    "Argentina": 100,
    "Brasil": 200,
    "Colombia": 300,
    "Chile": 400,
    "Ecuador": 500,
    "Bolivia": 600,
    "Jamaica": 700
}

print("Diccionario de países:")
print(paises)

paises["Brasil"] = 250

paises["Chile"] = 450

paises.update({"Bolivia": 650})

paises.update({"Jamaica": 750})

print("\nDiccionario modificado:")
for key, value in paises.items():
    print(f"{key}: {value}")
