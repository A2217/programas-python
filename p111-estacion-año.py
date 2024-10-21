# Estacion del año
def estacion(n):
    if n==1:
        est='Primavera'
    elif n==2:
        est='Verano'
    elif n==3:
        est='Otoño'
    elif n==4:
        est='Invierno'
    else:
        est=''
    return est

n = int(input('Dame la estacion del año (1-4) ? '))
print(f'La estacion del a#o es {estacion(n)}')