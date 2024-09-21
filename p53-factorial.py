# Imprime el factorial de un número

print("Calcula el factorial de un número \n")

n = int(input("Ingresa el número del cuál deseas factorial? "))
f = 1
for i in range(1,n+1):
    f = f * i

print(f"\nEl factorial es: {f}")
