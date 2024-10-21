# Suma números en un rango

def suma_rango(ini, fin):
    s = 0
    for i in range(ini, fin+1):
        s += i
    return s
print(f'{suma_rango(1,3)}')