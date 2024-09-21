# Imprime las tablas de la tabla 1 a la tabla n

print("Imprime las tablas de multiplicar de 1 a la tabla n\n")

n = int(input("Hasta cuál tabla quieres imprimir?: "))
m = int(input("Hasta qué número quieres multiplicar?: "))

for i in range(1,n+1):
    for j in range(1,m+1):
        print(f'{i} x {j} = {i*j}')
    print("\n")
