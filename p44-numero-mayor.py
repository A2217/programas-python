#Calcula el número mayor de una serie de números introducidos

while True:
    print("Encuentra el número mayor de una serie de números.")
    print("Introduce números separados por enter. Introduce [0] para detener.")

    mayor = -1  

    while True:
        n = int(input("Introduce un número: "))
        
        if n == 0:  
            break

        if n > mayor:  
            mayor = n
    
    if mayor == -1:
        print("\nNo se ingresaron números positivos para comparar.")
    else:
        print(f"\nEl número mayor ingresado es: {mayor}")

    r = input("\n¿Deseas repetir el proceso? [S]/[N]: ")
    if r.upper() == "N":
        print("Saliendo...")
        break
