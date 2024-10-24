# Función que suma pares o impares en un rango
def sumar_pares_impares(inicio, fin, tipo):
    suma = 0
    if tipo == 'P': 
        for num in range(inicio, fin+1):
            if num % 2 == 0:
                suma += num
    elif tipo == 'I': 
        for num in range(inicio, fin+1):
            if num % 2 != 0:
                suma += num
    return suma

# Programa principal
while True:
    print("\nMenú de opciones")
    print("[1] Sumar números pares en un rango")
    print("[2] Sumar números impares en un rango")
    print("[3] Salir")

    opcion = int(input("\nElige una opción [1-3]: "))

    if opcion in [1, 2]:
        inicio = int(input("Ingresa el inicio del rango: "))
        fin = int(input("Ingresa el fin del rango: "))
        
        if opcion == 1:
            resultado = sumar_pares_impares(inicio, fin, 'P')
            print(f"\nLa suma de los números pares entre {inicio} y {fin} es: {resultado}")
        else:
            resultado = sumar_pares_impares(inicio, fin, 'I')
            print(f"\nLa suma de los números impares entre {inicio} y {fin} es: {resultado}")
    
    elif opcion == 3:
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, elige entre 1 y 3.")
