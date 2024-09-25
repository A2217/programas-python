#Imprime la secuencia de números mostrados el numero de renglones que el usuario desee

renglones = int(input("¿Cuántos renglones deseas imprimir?: "))

for i in range(1, renglones+1):
    for j in range(1, i+1): 
        print(j, end=" ") 
    print()  