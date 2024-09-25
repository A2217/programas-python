# imprime los pares de 2 a n y su suma

n = int(input("Introduce el valor de n: "))

suma = 0  

for i in range(2, n+1, 2):
    print(i)
    suma += i  

print(f"La suma de los números pares es: {suma}")