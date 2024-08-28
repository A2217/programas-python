#Conversión de temperaturas de centigrados a Fahrenheit

print("Conversión de temperaturas de centigrados a Fahrenheit y viceversa \n")
print("[1] Convertir Celcius")
print("[2] Convertir Fahrenheit")
print("[3] Salir")

op = int(input("Elige la opción: \n"))

if op == 1:
    print("\nConvirtiendo Fahrenheit a Centigrados\n")
    t = float(input("Ingresa los grados Fahrenheit: "))
    r = (t - 32) * 5 / 9
    print(f'{t}° Fahrenheit, equivalen a {r:.2f}° Centigrados')
elif op == 2:
    print("\nConviritiendo Centigrados a Fahrenheit\n")
    t = float(input("Ingresa los grados Centigrados"))
    r = ( t * 9 / 5 ) + 32
    print(f"{t}° Fahrenheit, equivalen a {r:.2f}° Centigrados")
elif op == 3:
    print("\nSaliendo del programa... ")
else:
    print("Opción erronea")

print("\nProceso terminado.")