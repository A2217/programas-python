# Estudiante

estudiante = {
    "nombre":"Juan Perez",
    "edad":45,
    "email":"jperez@msn.com",
    "carrera":"Sistemas"
}

print(f"\nEl diccionario: \n\n{estudiante}")

estudiante["calificacion"]=9.5
estudiante["email"]="juanp@gmail.com"
print(f"\nEl diccionario actualizado: \n\n{estudiante}")

print("\nLas llaves: \n")
for k in estudiante.keys():
    print(k)

print("\nLos valores: \n")
for v in estudiante.values():
    print(v)

print("\nLlaves y valores:\n")
for k,v in estudiante.items():
    print(f"{k:<10} : {v}")