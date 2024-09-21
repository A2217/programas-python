# Imprime pirámide de un caracter determinado

print("Imprime pirámide de un caracter determinado \n")

n = int(input("De cuantos renglones quieres la pirámide? "))
car = input("Cuál caracter quieres usar para la pirámide? ")

for i in range(1,n+1):
    for j in range(1,i+1):
        print(car, end="")
    print("\r")