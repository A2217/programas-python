#Imprime la secuencia de términos armónicos el numero de renglones que el usuario desee y su suma

import math  

n = int(input("¿Cuántos términos?: "))

suma = 0
resultado = "Salida: "

for i in range(1, n+1):
    termino = 1 / math.factorial(i)  
    suma += termino  
    
    if i == 1:
        resultado += "1"
    else:
        resultado += f" + 1/{i}!"


print(f"{resultado}, suma: {suma}")
