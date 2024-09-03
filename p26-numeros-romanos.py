#Convierte un número del 1 al 10 en si equivalente a romano

print("Convierte un número del 1 al 10 en si equivalente a romano")
n = int(input("Ingresa un número: "))

if n == 1:
    print(f"{n} = I")
elif n == 2:
    print(f"{n} = II")
elif n == 3:
    print(f"{n} = III")
elif n == 4:
    print(f"{n} = IV")
elif n == 5:
    print(f"{n} = V")
elif n == 6:
    print(f"{n} = VI")
elif n == 7:
    print(f"{n} = VII")
elif n == 8:
    print(f"{n} = VIII")
elif n == 9:
    print(f"{n} = IX")
elif n == 10:
    print(f"{n} = X")
else:
    print(f"Error {n} número invalido")