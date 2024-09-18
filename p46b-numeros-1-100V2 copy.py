# Imprime los números desde 1 a n con for

print("Números del 1 a m con for")
m = int(input("Hasta donde quieres contar?: "))

for n in range(1,m+1,1):
    print(n,end="\n")