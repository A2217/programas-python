#Imprime los números de 100 a n con m incrementos

print("Contando desde 100 a n\n")
n = int(input("Ingresa el número hasta el que quieras contar: "))
m = int(input("Ingresa el multiplo en que se va a restar: "))

c = 100
while c >= n:
    print(c, end=" ")
    c = c - m