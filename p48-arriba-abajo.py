# Imprimir numeros del 1 a n o de n a 1

print("Imprimir los números de 1 a n o de n a 1\n")

while(True):   
    print("[1] Números de 1 a n")
    print("[2] Números de n a 1")
    op = int( input("\nIngresa una opción? ") )
    n = int(input("\nIngresa el limite n? "))

    if op==1:
        print(f"\nImprimiendo los numeros de 1 hasta {n}\n")
        for x in range(1,n+1,1):
            print(x,end=" ")

    elif op==2:
        print(f"\nImprimiendo los numeros de {n} hasta 1\n")
        for x in range(n,0,-1):
            print(x,end=" ")

    else:
        print("**Opción inválida**\n")
        continue

    res = input("\n\nDeseas continuar (S/N) ? ").upper()
    if res=="N":
        print("Saliendo...")
        break