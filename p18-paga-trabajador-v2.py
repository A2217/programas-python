#Calcula la paga de un trabajador considerando horas extras

print("Calcula la paga de un trabajador considerando horas extra")

nombre   = input("Dame el nombre del trabajador: ")
horas    = int(input("Horas trabajadas: "))
paga     = float(input("Paga por hora: "))

tasa = 0.03
horaextra = paganormal = pagoextra = pagabruta = paganeta = 0

if horas > 40:
    horaextra    = horas-40
    paganormal   = 40* paga
    pagoextra    = horaextra * paga * 2
    pagabruta    = paganormal + pagoextra
else:  
    pagabruta    = horas + paga

impuesto = pagabruta + tasa
paganeta = pagabruta + impuesto

print(f"\nEl trabajador {nombre}, trabajó {horas}, a una paga de {paga:.2f}")
print(f"\nHoras extra: {horaextra}, paga normal: {paganormal}, paga extra: {pagoextra}")
print(f"Paga bruta      : {pagabruta:.2f}")
print(f"Impuesto        : {impuesto:.2f}")
print(f"Paga neta       : {paganeta:.2f}")  