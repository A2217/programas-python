# numeros de 1 a 200, hasta dar la suma de 100

print("Imprime números hasta llegar a una suma de 100")

c = 0
s = 0

while c < 300 :
    c = c + 1
    s = s + c
    print(c,end=" ")
    if s >= 100 :
        print("\n")
        break

print(f"Se alcanzó el límite {s}, sumando {c} números")