#Genera pares de cada color

colores = input("Ingrese los colores separados por comas: ").split(",")

print("\nLos colores", colores)

for c1 in colores:
    for c2 in colores:
        if c1 != c2:
            print(f"{c1.strip()} y {c2.strip()}")