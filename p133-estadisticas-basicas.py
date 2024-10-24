# Calculo de datos estadisticos con funciones
import math

def leer_arreglo():
    nums = input("Dame los números separados por espacios: ").split()
    lista = []
    for num in nums:
        lista.append(int(num))  
    return lista

def mayor(lista):
    mayor_valor = lista[0]
    for num in lista:
        if num > mayor_valor:
            mayor_valor = num
    return mayor_valor

def menor(lista):
    menor_valor = lista[0]
    for num in lista:
        if num < menor_valor:
            menor_valor = num
    return menor_valor

def media(lista):
    suma = 0
    for num in lista:
        suma += num  
    return suma / len(lista) 

def varianza(lista):
    m = media(lista)
    suma_cuadrados = 0
    for x in lista:
        suma_cuadrados += (x - m) ** 2  
    return suma_cuadrados / len(lista)  

def desviacion_estandar(lista):
    return math.sqrt(varianza(lista)) 

# Programa principal
numeros = leer_arreglo()  

med = media(numeros)
may = mayor(numeros)
men = menor(numeros)
var = varianza(numeros)
desv_est = desviacion_estandar(numeros)

print(f"\nLista de números: {numeros}")
print(f"La media: {med:.3f}")
print(f"Mayor de los datos: {may}")
print(f"Menor de los datos: {men}")
print(f"Varianza: {var:.3f}")
print(f"Desviación estándar: {desv_est:.3f}")
