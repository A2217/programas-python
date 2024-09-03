#Dado un numero entero entre 1 y 7, se desea mostrar
#con letra el día de la semana correspondiente, 1 es
#domingo,2 es lunes y así hasta 7 es viernes. 
#Si el número no está en el rango especificado, 
#mostrar un mensaje de error.
#Ej: 1 , Lunes, Ej 8 , dia inválido

print("Calculando el día de la semana de acuerdoa un número")
n = int(input("Ingresa un número del 1 al 7: "))

if n == 1:
    print("El día es domingo")
elif n == 2:
    print("El día es lunes")
elif n == 3:
    print("El día es martes")
elif n == 4:
    print("El día es miercoles")
elif n == 5:
    print("El día es jueves")
elif n == 6:
    print("El día es viernes")
elif n == 7:
    print("El día es sabado")
else:
    print(f"Error {n} día invalido")