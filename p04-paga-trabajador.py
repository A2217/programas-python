#p04-paga-trabajador - El programa calcula la paga de un trabajador

print("Calculando la paga de un trabajador :\n")

nombre = input("Dame el nombre del trabajador")
horas = int(input("Horas ?"))
paga = float(input("paga x hora"))
tasa = 0.03

pagabruta = paga * horas
impuesto = pagabruta * tasa
paganeta = pagabruta - impuesto

print(f"El trabajador {nombre}, trabajó {horas} a una paga de {paga} con una tasa de {tasa}")
print(f"Paga bruta : {pagabruta:,.2f}")
print(f"Impuesto : {impuesto:,.2f}")
print(f"Paga neta : {paganeta:,.2f}")
