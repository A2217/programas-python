class Articulo:
    def __init__(self, id, descripcion, cantidad, precio):
        self.id = id
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio = precio

    def obtenerTotal(self):
        return self.cantidad * self.precio

    def __str__(self):
        return (f"id={self.id}, descripcion={self.descripcion}, cantidad={self.cantidad}, "
                f"precio={self.precio:.2f}, total={self.obtenerTotal():.2f}")

# Programa principal
import os
os.system('cls')
art1 = Articulo('A101', 'Pluma Roja', 888, 0.08)
print(art1)

art1.cantidad = 999
art1.precio = 0.99
print("id           = ", art1.id)
print("descripcion  = ", art1.descripcion)
print("cantidad     = ", art1.cantidad)
print("precio       = ", art1.precio)
print("total        = ", art1.obtenerTotal())

art2 = Articulo("A102", "Pluma Azul", 934, 1.2)
print(art2)

art3 = Articulo("P103", "Lapiz del 12", 456, 0.5)
print(art3)

total = art1.obtenerTotal() + art2.obtenerTotal() + art3.obtenerTotal()
print('Total todos:', total)
