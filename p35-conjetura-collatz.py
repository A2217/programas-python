# Calcula la conjetura de Collatz

while(True):
    
    print("Imprime la conjetura de collatz")
    n = int(input("Ingresa un número= "))
    pasos = int(0)

    while n != 1:
        print(n,end=" ")

        if n % 2 == 0:
            n = n // 2
            
        else:
            n = 3 * n + 1

        pasos +=1

    
    print(n,end=" ")
    r=input(f"\nSe realizaron {pasos} \n con Deseas Continuar [S]/[N]?: ")

    if r.upper()=="N":
        print("Saliendo...")
        break