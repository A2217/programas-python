# suma de n números introducidos por el usuario:

while(True):

    print("Suma de n números introducidos por el usuario:")

    c = int(input("Cuantos números?: "))
    suma = 0

    for i in range(1,c+1):
        n = int(input(f"Número {i}: "))
        suma += n

    print(f"\nLa suma es {suma}")

    res = input("\n\nDeseas continuar (S/N) ? ").upper()
    if res=="N":
        print("Saliendo...")
        break