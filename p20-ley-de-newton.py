# segunda ley de newton (fuerza = masa * aceleracion)

print("Calcula los valores de la segunda ley de Newton")
print("[1] Calcular la fuerza")
print("[2] Calcular la masa")
print("[3] Calcular la aceleración\n")

op = int(input("Elge una opción: "))

if op == 1:
    print("\nCalculando la fuerza")
    m = int(input("Ingresa la masa:  "))
    a = int(input("Ingresa la aceleración: "))
    f = m * a
    print(f'la fuerza es {f}')
elif op == 2:
    print("\nCalculando la masa")
    f = int(input("Ingresa la fuerza: "))
    a = int(input("Ingresa la aceleración: "))
    m = f / a
    print(f"La masa es: {m}")
elif op == 3:
    print("\nCalculando la aceleración")
    f = int(input("Ingresa la fuerza: "))
    m = int(input("Ingresa la masa: "))
    a = f / m
    print(f"La aceleración es {a}")
else :
    print("*Opcion invalida*")