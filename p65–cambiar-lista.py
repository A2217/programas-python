# Cambiar los elementos de una lista

n = [10, 9, 8.5, 6.5, 9.8, 7, 5, 6.2, 9.5]

print(f"todos los números : {n}\n")

n[0]=7
n[1]=7
print(f"modificar 0 y 1 : {n}\n")

n[2:5] = [9,9,9]
print(f"modificar 2:5 - : {n}\n")