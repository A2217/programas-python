#Calcula el número de la suerte

año = int(input("Ingresa tu año de nacimiento: "))

suma = 0

while año > 0:
    suma = suma + (año % 10)
    año = año // 10

print(f"Tu número de la suerte es: {suma}") 
