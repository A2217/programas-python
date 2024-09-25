# Remover elementos de la lista

n = [1, 3, 5, 7, 9, 11, 99, 15, 88, 19, 100]
print(f"todos los números : {n}\n")

n.remove(99)
print(f"remover primera ocurrencia : {n}\n")

num=n.pop(8)
print(f"remover y regresar elemento : {n} - {num}\n")

num=n.pop()
print(f"remover el ultimo: : {n} - {num}\n")

n.clear()
print(f"remover todos : {n}\n")