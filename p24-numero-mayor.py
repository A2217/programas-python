#Dados tres números enteros, verificar cual es el mayor,
#ej: 10, 9 8, el mayor es 10, 11, 30, -1 el mayor es 30

print("Verifica cuál de los tres números es mayor")
print("Dame 3 números enteros separados por un espacio: ")

n1,n2,n3 = input().split()
n1,n2,n3 = [int(n1),int(n2),int(n3)]

if n1 > n2 and n1 > n3:
    print(f"{n1} es mayor que {n2} y {n3}")
elif n2 > n1 and n2 > n3:
    print(f"{n2} es mayor que {n1} y {n3}")
else:
    print(f"{n3} es mayor que {n1} y {n2}")