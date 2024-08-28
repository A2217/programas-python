#Calcula la paga de un trabajador considerando horas extras

print("Calcula la paga de horas extra de un trabajador (se pagan al doble)")

nombre = input("Dame el nombre del trabajador: ")
horas = int(input("Horas trabajadas: "))
paga = int(input("Paga por hora: "))
if horas > 40 :
    extra = horas - 40
    total = (40 * paga ) + ( extra * (paga + paga))
    pe = extra*paga*2
    print(f"{nombre} trabajo {horas} horas, con una paga de {paga}, horas extra trabajadas {extra}  total de pago {total} del cual {pe} fueron extra")
else :
    total = horas * paga
    print(f"{nombre} trabajo {horas} horas, con una paga de {paga}, total de pago {total}")