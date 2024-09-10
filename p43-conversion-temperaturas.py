#Calcula la temperatura de centigrados a fahrenheit en un rango de valores

while True:
    print("Conversión de temperaturas de grados Celsius a Fahrenheit.")
    temp_inicial = int(input("Introduce la temperatura inicial en grados Celsius: "))
    temp_final = int(input("Introduce la temperatura final en grados Celsius: "))

    if temp_inicial > temp_final:
        print("Error: La temperatura inicial debe ser menor o igual a la temperatura final.")
        continue

    print("\nTemperaturas convertidas:")
    celsius = temp_inicial
    while celsius <= temp_final:
        fahrenheit = (9/5) * celsius + 32
        print(f"{celsius} °C = {fahrenheit:.2f} °F")
        celsius += 1

    r = input("\n¿Deseas repetir el proceso? [S]/[N]: ")
    if r.upper() == "N":
        print("Saliendo...")
        break