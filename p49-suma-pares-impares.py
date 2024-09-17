# pares e impares de 1 a n y su suma

print("\nPares e impares de 1 a n y su suma \n")

while(True):
    n = int(input("Hasta dónde quieres contar? "))
    s = 0
    print("\nNumeros pares:")
    for i in range(1,n+1,2):
        print(i,end=" ")
        s += i
    print(f"\nSuma de los números pares: {s}")

    s = 0
    print("\nNumeros impares:")
    for i in range(2,n+1,2):
        print(i,end=" ")
        s += i
    print(f"\nSuma de los números impares: {s}")

    res = input("\n\nDeseas continuar (S/N) ? ").upper()
    if res=="N":
        print("Saliendo...")
        break