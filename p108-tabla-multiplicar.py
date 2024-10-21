# Tabla de multiplicar
def tabla_multiplicar(t, n):
    for i in range(1, n+1):
        print(f'{t} x {i} = {t * i}')

t = int(input('Que tabla deseas? '))
n = int(input('Hasta donde? '))
tabla_multiplicar(t, n)