# imprime secuencia de números mostrados el número de renglones que el usuario desee

renglones = int(input("¿Cuántos renglones deseas imprimir?: "))

numero = 1  

for i in range(1, renglones+1):
    for j in range(i):  
        print(i, end=" ")  
        
    print() 