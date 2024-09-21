# Imprime el factorial de n números

print("Imprime el factorial desde 1 a n números\n")

while(True):
    n = int(input("Hasta cuál número deseas imprimir el factorial? "))

    for i in range(1,n+1):
        f=1
        print(f"{i}! = ", end="")

        for i in range(1,i+1):
            f *= i
        print(f)

    res = input("\n\nDeseas continuar (S/N) ? ").upper()
    if res=="N":
        print("Saliendo...")
        break