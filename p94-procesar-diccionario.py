# Listas de nombres y sueldos
nombres = ["Juan", "Pedro", "Manuel", "Elias", "Maria", "Felipe", "Julia", "Roberto"]
sueldos = [4550.22, 8456.88, 1235.12, 9998.00, 12345.50, 29456.55, 12234.00, 2000.00]

trabajadores = dict(zip(nombres, sueldos))

print("Diccionario de trabajadores:")
print(trabajadores)

print("\nUsando keys():")
for nombre in trabajadores.keys():
    print(nombre)

print("\nUsando values():")
for sueldo in trabajadores.values():
    print(sueldo)

print("\nUsando llave y valor:")
for nombre in nombres:
    print(f"{nombre}: {trabajadores[nombre]}")

print("\nUsando items():")
for nombre, sueldo in trabajadores.items():
    print(f"{nombre}: {sueldo}")

suma_sueldos = sum(trabajadores.values())
print(f"\nLa suma de los sueldos es: {suma_sueldos}")

promedio_sueldos = suma_sueldos / len(trabajadores)
print(f"El promedio de los sueldos es: {promedio_sueldos:.2f}")
