# Imprime los números del 100 a n con for con k decrementos

print("Numeros del 100 a m con for")
m = int(input("Hasta donde quieres contar?: "))
k = int(input("En decrementos k de?: "))

for n in range(100,m-1,-k):
    print(n,end="\n")