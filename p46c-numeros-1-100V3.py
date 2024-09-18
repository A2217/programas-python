# Imprime los números desde 0 a n con for con k incrementos

print("Números del 0 a m con for")
m = int(input("Hasta donde quieres contar?: "))
k = int(input("En incrementos k de?: "))

for n in range(1,m+1,k):
    print(n,end="\n")