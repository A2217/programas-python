# Calcular cantidad de productos y subtotal por cliente

n = int(input("Número de compras: "))
compras = []

for i in range(1, n+1):
    print(f"\n------ Compra {i} ------")
    compra = {
        "cliente": input("Nombre Cliente: "),
        "producto": input("Nombre Producto: "),
        "cantidad": int(input("Cantidad: ")),
        "precio": float(input("Precio: "))
    }
    compras.append(compra)

print("\nDiccionario de compras:\n", compras)

clientes = {}

for compra in compras:
    cliente = compra["cliente"]
    if cliente not in clientes:
        clientes[cliente] = {"cantidad": 0, "subtotal": 0}
    
    clientes[cliente]["cantidad"] += compra["cantidad"]
    clientes[cliente]["subtotal"] += compra["cantidad"] * compra["precio"]

print("\nLos clientes y sus totales:\n")
for cliente, datos in clientes.items():
    print("Cliente :", cliente)
    print("Cantidad total de productos:", datos["cantidad"])
    print("Subtotal:", datos["subtotal"])
    print()

print("\nDiccionario de clientes: \n", clientes)
