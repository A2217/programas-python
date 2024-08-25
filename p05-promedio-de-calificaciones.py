#Calcula-el-promedio-de-3-calificaciones

print('Calculando el promedio de 3 calificaciones')

print('Dame 3 calificaciones separadas por espacios')
c1,c2,c3 = input().split()
c1,c2,c3 = [int(c1),int(c2),int(c3)]

prom = (c1+c2+c3)/3

print(f'El promédio de : {c1},{c2},{c2} es {prom}')