# Muestra al tipo de angulo
# <90 agudo, =90 recto, >90 y <180 obtuso, =180 llano, >180 y <360 concavo

print("Mostrando el tipo de ángulo en base a los grados")
angulo = int(input("Ingresa el ángulo: "))
print(f"El ángulo tiene {angulo} grados por lo tanto es un ángulo: ",end="")

if angulo>=0 and angulo <=360:
    if angulo < 90 :
        print("Agudo")
    elif angulo == 90 :
        print("Recto")
    elif angulo > 90 and angulo < 180 :
        print("Obtuso")
    elif angulo == 180 :
        print("Llano")
    elif angulo > 180 and angulo < 360 :
        print("Concavo")
    else:
        print("Cerrado o completo")
else :
    print("\nángulo fuera de rango")