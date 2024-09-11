#Control de ventas del evento académico

print("Universidad Chafa SA de CV")
print("Sistema de inscripción Congreso de Sistemas")

total_ventas_dia = 0  

while True:        
    print("\nSelecciona el tipo de usuario:")
    print("[1] Alumno $100")
    print("[2] Trabajador $200")
    print("[3] Docente $500")
    tipo_usuario = int(input("Tipo de usuario? "))
    
    if tipo_usuario == 1:
        precio_usuario = 100
        nombre_usuario = "Alumno"
    elif tipo_usuario == 2:
        precio_usuario = 200
        nombre_usuario = "Trabajador"
    elif tipo_usuario == 3:
        precio_usuario = 500
        nombre_usuario = "Docente"
    else:
        print("**Error. Tipo de usuario inválido. Reinicia el proceso**")
        continue
    
    print("\nSelecciona el tipo de paquete:")
    print("[1] Solo conferencias $600")
    print("[2] Con eventos sociales $800")
    print("[3] Con kit de acceso $900")
    tipo_paquete = int(input("Tipo de paquete? "))
    
    if tipo_paquete == 1:
        precio_paquete = 600
        nombre_paquete = "Solo conferencias"
    elif tipo_paquete == 2:
        precio_paquete = 800
        nombre_paquete = "Con eventos sociales"
    elif tipo_paquete == 3:
        precio_paquete = 900
        nombre_paquete = "Con kit de acceso"
    else:
        print("**Error. Tipo de paquete inválido. Reinicia el proceso**")
        continue
    
    cantidad = int(input("\nCantidad de inscripciones? "))
    
    subtotal = (precio_usuario + precio_paquete) * cantidad
    
    descuento = 0  
    porcentaje_descuento = 0  
    if subtotal > 5000:
        if tipo_usuario == 1:  # Alumno
            descuento = subtotal * 0.20
            porcentaje_descuento = 20
        elif tipo_usuario == 2:  # Trabajador
            descuento = subtotal * 0.10
            porcentaje_descuento = 10
        elif tipo_usuario == 3:  # Docente
            descuento = subtotal * 0.05
            porcentaje_descuento = 5
    
    total = subtotal - descuento
    
    print(f"\nTu pedido fue:\nCantidad de inscripciones {cantidad}\nTipo de usuario: {nombre_usuario}\nTipo de paquete: {nombre_paquete}")
    print(f"Subtotal: {subtotal:.2f}\nDescuento de: {descuento:.2f} ({porcentaje_descuento}%)\nCon un total de {total:.2f}")
  
    total_ventas_dia += total
    
    r = input("\n¿Deseas procesar otra inscripción? [S]/[N]: ")
    if r.upper() == "N":
        print(f"\nTotal de ventas del día: ${total_ventas_dia:.2f}")
        print("Saliendo...")
        break