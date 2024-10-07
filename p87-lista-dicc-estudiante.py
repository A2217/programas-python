# Estudiantes y sus datos, en una Lista de Diccionarios

grupo = [
    {"nombre": "Carlos", "edad": 45, "carrera": "sistemas", "promedio": 9},
    {"nombre": "Rocio", "edad": 35, "carrera": "sistemas", "promedio": 10}
]

print(f"Grupo original: {grupo}")

while True:
    print(f"\nDatos Estudiante:")
    datos = {}  
        
    nombre = input("Nombre? ")
    if nombre != "":
        datos["nombre"] = nombre
        datos["edad"] = int(input("Edad? "))
        datos["carrera"] = input("Carrera? ")
        datos["promedio"] = float(input("Promedio? "))
        grupo.append(datos)  
    else:
        break

print(f"\nGrupo completo: {grupo} - {len(grupo)} estudiantes")

print("\nDatos en forma de Tabla:\n")

for k in grupo[0].keys():
    print(f"{k}\t", end=" ")
print()

for alumno in grupo:
    for v in alumno.values():
        print(f"{v}\t", end=" ")
    print()  

print("\nDatos en forma de Registro:\n")

s = 0 
for est in grupo:
    s += est["promedio"]      
    for k, v in est.items():
        print(f"{k:<10} : {v}")
    print(" ")  

p = s / len(grupo)
print(f"La suma de los promedios es: {s}")
print(f"El promedio general es: {p:.2f}")
