# Segundo examen parcial
empleados = []
print("Mueblería Muebles Dico")
print("Sistema de Procesamiento de Empleados")
print("Captura de datos de los empleados")

def es_nombre_valido(nombre):
    return nombre.isalpha()

def es_edad_valida(edad):
    return edad.isdigit() and int(edad) > 0

def es_sexo_valido(sexo):
    return sexo.lower() in ['m', 'f']

def es_sueldo_valido(sueldo):
    try:
        return float(sueldo) > 0
    except ValueError:
        return False

while True:
    nombre = input("Nombre del empleado (Para terminar presiona solo enter): ")
    if not nombre:
        break
    while not es_nombre_valido(nombre):
        nombre = input("Por favor, ingrese un nombre válido (solo letras): ")
    
    edad = input(f"Edad de {nombre}: ")
    while not es_edad_valida(edad):
        edad = input(f"Por favor, ingrese una edad válida (número positivo): ")
    edad = int(edad)
    
    sexo = input(f"Sexo de {nombre} (m o f): ")
    while not es_sexo_valido(sexo):
        sexo = input(f"Por favor, ingrese un sexo válido (m o f): ")
    
    pasatiempos = input(f"Pasatiempos de {nombre} (separados por una coma y un espacio): ").split(', ')
    while not all(pasatiempo.strip() for pasatiempo in pasatiempos):
        pasatiempos = input(f"Por favor, ingrese pasatiempos válidos para {nombre} (separados por una coma y un espacio): ").split(', ')
    
    sueldo = input(f"Sueldo de {nombre}: ")
    while not es_sueldo_valido(sueldo):
        sueldo = input(f"Por favor, ingrese un sueldo válido (número positivo): ")
    sueldo = float(sueldo)

    empleados.append({
        'nombre': nombre,
        'edad': edad,
        'sexo': sexo,
        'pasatiempos': pasatiempos,
        'sueldo': sueldo
    })

print("\nDatos almacenados en la lista de diccionarios:")
for empleado in empleados:
    print(empleado)

print("\nTabla de datos:")
print(f"{'Nombre':<10} {'Edad':<5} {'Sexo':<10} {'Salario':<10} {'Pasatiempos'}")
for empleado in empleados:
    pasatiempos_str = ', '.join(empleado['pasatiempos'])
    sexo_str = 'Masculino' if empleado['sexo'] == 'm' else 'Femenino'
    print(f"{empleado['nombre']:<10} {empleado['edad']:<5} {sexo_str:<10} {empleado['sueldo']:<10.2f} {pasatiempos_str}")

total_empleados = len(empleados)
hombres = sum(1 for e in empleados if e['sexo'] == 'm')
mujeres = total_empleados - hombres

pasatiempos_contador = {}
for empleado in empleados:
    for pasatiempo in empleado['pasatiempos']:
        if pasatiempo in pasatiempos_contador:
            pasatiempos_contador[pasatiempo] += 1
        else:
            pasatiempos_contador[pasatiempo] = 1

suma_edad = sum(e['edad'] for e in empleados)
promedio_edad = suma_edad / total_empleados if total_empleados > 0 else 0
suma_sueldo = sum(e['sueldo'] for e in empleados)
promedio_sueldo = suma_sueldo / total_empleados if total_empleados > 0 else 0
mayor_empleado = max(empleados, key=lambda e: e['edad'])
menor_empleado = min(empleados, key=lambda e: e['edad'])

print("\nResumen:")
print(f"Empleados : {total_empleados}")
print(f"Hombres : {hombres}")
print(f"Mujeres : {mujeres}")
print("Pasatiempos:", ', '.join([f"{p}/{c}" for p, c in pasatiempos_contador.items()]))
print(f"Edad -> suma: {suma_edad}, Promedio: {promedio_edad:.1f}")
print(f"Sueldo -> suma: {suma_sueldo:.2f}, Promedio: {promedio_sueldo:.2f}")
print(f"{mayor_empleado['nombre']} de {mayor_empleado['edad']} es el mayor, {menor_empleado['nombre']} de {menor_empleado['edad']} es el menor.")
