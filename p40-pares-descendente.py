#Imprime los npúmeros impares de forma descendetne desde 100 a n

print("Imprime los números impares de forma descendente desde 100 a n y suma el total de los números impresos")

while(True):    
    n = int(input("Hasta dónde quieres contar?: "))
    m = 99 # Comienza desde el primer número impar menor que 100
    suma = 0

    if n % 2 == 0:
        print("Error, el número no es impar. Ingresa otro número")
        
    else:
        while m >= n:    
            print(f"{m}")        
            if m %2 !=0:
                suma = suma + m                
                m -= 2 
                
                
    print(f"La suma de los números impares es {suma}")

    r=input("\nDeseas Continuar [S]/[N]? ")
    if r.upper()=="N":
        print("Saliendo...")
        break