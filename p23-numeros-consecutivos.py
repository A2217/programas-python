#Dados tres números enteros, verificar si son consecutivos 
#(9,10,11) y mandar mensaje confirmándolo, si no lo son
#(1,4,6) mandar mensaje de error.

print("Verifica si los tres números son consecutivos")
print("Dame 3 números enteros separados por un espacio: ")

n1,n2,n3 = input().split()
n1,n2,n3 = [int(n1),int(n2),int(n3)]

if n1 < n2 and n1 < n3 and n2 < n3:
    print(f"Los números {n1}, {n2}, {n3} son consecutivos")
else:
    print(f"Error los números {n1}, {n2}, {n3} no son consecutivos")