#Calcula la suma y le promedio de una serie de números

while True:
    print("Calcula la suma y promedio de los números introducidos")
    print("Agrega [0] para detenerse")
    print("Agrega los números separados por Enter:")

    contador = 0
    suma = 0

    while True:
        n = int(input())
        if n == 0:  
            break
        suma += n
        contador += 1

    if contador > 0:  # Asegurarse de no dividir por cero
        prom = suma / contador
        print(f"La suma total es {suma}")
        print(f"El promedio de los números ingresados es {prom}")
        print(f"Se ingresaron {contador} números")
    else:
        print("No se ingresaron números para calcular el promedio.")

    r = input("\n¿Deseas continuar [S]/[N]? ")
    if r.upper() == "N":
        print("Saliendo...")
        break