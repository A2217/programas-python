# tabla de multiplicar con for

print("Imprime una tabla de multiplicar usando for\n")

while(True):
    t = int(input("De cuál número quieres imprimir la tabla?: "))
    n = int(input("Hasta qué número quieres multiplicar?: "))

    for i in range(1, n+1):
        print(f"{t} x {i} = {t*i}")

    res = input("\n\nDeseas continuar (S/N) ? ").upper()
    if res=="N":
        print("Saliendo...")
        break