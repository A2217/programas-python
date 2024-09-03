# aceptar estudiante en base a cierto criterios

print("Universidad Kitty Kat SA")
nombre = input("Ingresa tu nombre: ")
sexo = input("Ingresa tu genero [M] o [F]: ")
edad = int(input("Ingresa tu edad: "))

if sexo == "M":
    print("Solo se aceptan a mujeres")
elif sexo == "F": 
    if edad < 21:
        print("Eres mujer, pero no tienes la edad, solo mayores de 21 años")
    else:
        print("Ingresa 3 calificaciones separadas por espacio:  ")
        c1,c2,c3 = input().split()
        c1,c2,c3 = [int(c1),int(c2),int(c3)]
        prom = (c1+c2+c3)/3
        if prom >= 8 and prom <= 9.5:
            print(f"{nombre} Bienvenida a la Universidad Kitty Kat SA, tu edad {edad} y calificaciones {c1}, {c2} y {c3} lo permiten")
        elif prom > 9.5: #agregado por no querer rechazar a alguien con promedio arriba de 9.5
            print("Bienvenida a la Universidad Kitty Kat SA, tu excelencia académica te brindará apoyos económicos")
        else:
            print("Eres mujer, tienes la edad, pero tu promédio no alcanza, solo promedios de 8 a 9.5")
else: 
    print("Gracias por utilizar el programa")