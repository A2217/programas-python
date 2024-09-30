# mes, día y nombre
nombres_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
                 "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]


dias_meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

mes = int(input("Introduce el número del mes (1-12): "))

if 1 <= mes <= 12:
    nombre_mes = nombres_meses[mes - 1]  
    dias_mes = dias_meses[mes - 1]           

    print(f"El mes es {nombre_mes} y tiene {dias_mes} días.")
else:
    print("Número de mes inválido. Debe estar entre 1 y 12.")
