# Conversiones a metro

conversiones = {
'km': 1000, 
'm': 1, 
'cm': 0.01, 
'mm': 0.001  
}

longitud = int(input("Ingresa la longitud en metros que deseas convertir: "))

while True:
    unidad = input("Unidad (km, m, cm ,mm ? ")
    if unidad in conversiones:
        break

resultado = longitud * conversiones[unidad]
print(f"{longitud:,.2f} {unidad} son {resultado:,.2f} metros")