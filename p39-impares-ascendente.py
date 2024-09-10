#Imprime los npúmeros impares de forma ascendente desde 1 a n

print("Imprime los números impares y suma el total de los números impresos")

while(True):    
    n = int(input("Hasta dónde quieres contar?: "))
    m = 1 #inicializando en 1 por ser el primer número impar
    suma = 0

    if n % 2 == 0:
        print("Error, el número no es impar. Ingresa otro número")
        
    else:
        while m <= n:    
            print(f"{m}")        
            if m %2 !=0:
                suma = suma + m                
                m += 2 
                
                
    print(f"La suma de los números impares es {suma}")

    r=input("\nDeseas Continuar [S]/[N]? ")
    if r.upper()=="N":
        print("Saliendo...")
        break