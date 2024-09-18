# Imprime los números del 100 a n con for

print("Numeros del 100 a m con for")
m = int(input("Hasta donde quieres contar?: "))

for n in range(100,m-1,-1):
    print(n,end="\n")