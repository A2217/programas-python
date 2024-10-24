# Función que pide 3 números enteros y devuelve el menor
def menor_de_tres():
    n1 = int(input("Ingresa el primer número: "))
    n2 = int(input("Ingresa el segundo número: "))
    n3 = int(input("Ingresa el tercer número: "))
        
    if n1 < n2 and n1 < n3:
        return n1
    elif n2 < n1 and n2 < n3:
        return n2
    else:
        return n3

# Programa principal
men = menor_de_tres()

print("El número menor es:", men)