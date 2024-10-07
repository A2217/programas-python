# Leer la cadena del usuario
cadena = input("Ingresa una cadena: ")

contador = {}

for caracter in cadena:
    if caracter in contador:
       
        contador[caracter] += 1
    else:
        contador[caracter] = 1

print("Cantidad de apariciones de cada carácter:")
print(contador)
