# Procesar pizza

ingr = {"T": 1.50, "P": 3.50, "C": 3.74, "A": 0.40}
base = 15
st = 0
des = 0

pedido = input("Ingredientes de tu pizza?\n[T] para Tomate\n[P] para Pepperoni\n[C] para Champiñones\n[A] para Aceitunas\nIngresa todas las letras de los ingredientes que quieras: ").upper()

for i in pedido:
    if i in ingr:
        st += ingr[i]
des = (st * 0.05)
st += base  

if st >= 20:
    tot = st - (st * 0.05)  
else:
    tot = st

print(f"El subtotal es: {st:.2f}")
print(f"El descuento es: {des:.2f}")
print(f"El total es: {tot:.2f}")
