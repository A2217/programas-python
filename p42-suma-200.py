#Calcula la suma de los números ingresados hasta que la suma sea >= 200

while True:
    print("Calcula la suma de números hasta que sea mayor o igual a 200.")
    print("Introduce los números separados por Enter:")

    suma = 0
    contador = 0

    while suma < 200:  
        n = int(input())
        suma += n
        contador += 1

    print(f"\nLa suma total es {suma}")
    print(f"Se introdujeron {contador} números")

    r = input("\n¿Deseas repetir el proceso? [S]/[N]: ")
    if r.upper() == "N":
        print("Saliendo...")
        break
