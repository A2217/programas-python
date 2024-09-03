#Calcula el promedio de 5 calificaciones

print("Calculando el promédio de 5 calificaiones")

print("Ingresa las calificaciones separados por un espacio: ")

n1,n2,n3,n4,n5 = input().split()
n1,n2,n3,n4,n5 = [int(n1),int(n2),int(n3),int(n4),int(n5)]

p = (n1+n2+n3+n4+n5)/5
print(f"{p}")

if p >= 0 and p < 6:
    print(f"Promedio de {p:.2f}. Quedas reprobado")
elif p >= 6 and p < 7:
    print(f"Promedio de {p:.2f}. Pasas de panzazo")
elif p >= 7 and p < 8:
    print(f"Promedio de {p:.2f}. Muy bien, pues mejorar")
elif p >= 8  and p < 9:
    print(f"Promedio de {p:.2f}. Excelente sigue así")
elif p >= 9 and p <= 10:
    print(f"Promedio de {p:.2f}. Perfecto tu esfuerzo valió la pena")