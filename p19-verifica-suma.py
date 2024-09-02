#verifica si la suma de dos número es igual a un tercero

print("Verifica si la suma de dos números es igual a un tercero")
print("Dame 3 números enteros separados por un espacio: ")

n1,n2,n3 = input().split()
n1,n2,n3 = [int(n1),int(n2),int(n3)]

if   n1 + n2 == n3:
    print(f"{n1} + {n2} = {n3}")
elif n1 + n3 == n2:
    print(f"{n1} + {n3} = {n2}")
elif n2 + n3 == n3:
    print(f"{n2} + {n3} = {n1}")
elif n1 == n2 == n3:
    print(f"{n1} == {n2} == {n3}")
else:
    print(f"Los números so diferentes: {n1}, {n2}, {n3}")

print("Proceso terminado")