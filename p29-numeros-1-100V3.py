#Imprime los números del 0 a n en m incrementos

print("Imprime los números de 0 a n con m incrementos")
n = int(input("\nIngresa el valor de n: "))
m = int(input("\nIngresa el valor de m: "))
c = 0
while c <= n:
    print(c, end=" ")
    c = c + m