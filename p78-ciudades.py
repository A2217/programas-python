#Imprime nombre de ciudades

ciudades = []

while True:
    ciudad = input("Introduce el nombre de una ciudad (o $ para detenerse): ")
    if ciudad == "$":
        break
    ciudades.append(ciudad)


print(f"\nCantidad de ciudades introducidas: {len(ciudades)}")
print("Lista completa de ciudades:", ciudades)


ciudades.sort(reverse=True)
print("\nLista de ciudades ordenada en orden descendente:", ciudades)


def empieza_con_consonante(nombre):
    consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    return nombre[0] in consonantes


ciudades_consonante = [ciudad for ciudad in ciudades if empieza_con_consonante(ciudad)]
print(f"\nCantidad de ciudades que empiezan con consonante: {len(ciudades_consonante)}")
print("Ciudades que empiezan con consonante:", ciudades_consonante)
