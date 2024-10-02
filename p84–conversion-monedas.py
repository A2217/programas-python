# Conversiones a Pesos

conversiones = {
'USD': 20.50, 
'EUR': 22.30, 
'GBP': 25.80, 
'JPY': 0.19, 
'CAD': 16.20 
}
print("Conversor de monedas a pesos mexicanos")

print("\nOpciones de monedas: ")
for moneda in conversiones:
    print(f"- {moneda} ")

while True:
    moneda = input("\nIngrese la moneda a convertir a pesos mexicanos: ").upper()
    if moneda in conversiones: break

cantidad = float(input("Ingrese la cantidad a convertir: "))

resultado = cantidad * conversiones[moneda]
print(f"{cantidad:,.2f} {moneda} son {resultado:,.2f} MXN")