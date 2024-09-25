# Agregar elementos a la lista

print("Agregar elementos a una lista existente \n")

n = [80.3, 12.5, 60.2, 30.4]
print(f"todos los números : {n}\n")

n.append(90)
n.append(100)
print(f"agregar al final : {n}\n")

n.insert(4,80)
print(f"insertar : {n}\n")

otros = [110,120,130]
n.extend(otros)
print(f"extender con : {n}\n")