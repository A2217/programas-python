# Dado un día imprimir la paga correspondiente

print("Dado un día imprimir la paga correspondiente\n")

dias = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
paga = [100,200,300,400,500,600,700]
dia = " "

while True:
    dia = input("Dame un dia entre lunes y domingo ? ")
    if dia in dias:
        break

print(f"Elegiste el dia: {dia} ")
pos = dias.index(dia)
print(f"Que corresponde a un paga de: {paga[pos]}")