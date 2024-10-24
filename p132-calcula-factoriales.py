# Calcula el factorial con funciones
def leer_arreglo():
    nums = list(map(int, input("Dame los números separados por espacios: ").split()))
    return nums

def calcular_factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, num + 1):
            factorial *= i
        return factorial

def lista_factoriales(lista):
    factoriales = []
    for num in lista:
        factoriales.append(calcular_factorial(num))
    return factoriales

# Programa principal
numeros = leer_arreglo()  
factoriales_lista = lista_factoriales(numeros)  

print("\nLa lista de números originales:", numeros)
print("La lista con los factoriales:", factoriales_lista)
