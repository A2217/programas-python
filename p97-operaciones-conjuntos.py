# Operaciones entre conjuntos de números

c1 = {1, 2, 3, 4, 5}
c2 = {5, 6, 7, 8, 9, 10}
c3 = {9, 10, 11, 12, 13}
c4 = {3, 4, 5}

print(f"c1 : {c1}\nc2 : {c2}\nc3 : {c3}\nc4 : {c4}")

print("\nUnión: ")
print(f"c1 unión c2 : {c1.union(c2)}")
print(f"c1 unión c3 : {c1 | c3}")

print("\nIntersección: ")
print(f"c1 intersección c2: {c1.intersection(c2)}")
print(f"c2 intersección c3: {c2 & c3}")

print("\nDiferencia:")
print(f"c1 diferencia c4: {c1.difference(c4)}")
print(f"c2 diferencia c3: {c2 - c3}")

print("\nDiferencia simétrica:")
print(f"c1 diferencia simétrica c2: {c1.symmetric_difference(c2)}")
print(f"c2 diferencia simétrica c3: {c2 ^ c3}")

print("\nProbar por subconjuntos:")
print(f"c4 es subconjunto de c1? : {c4.issubset(c1)}")
print(f"c3 es subconjunto de c2? : {c3 <= c2}")

print("\nProbar por superconjuntos:")
print(f"c1 es superconjunto de c4? : {c1.issuperset(c4)}")
print(f"c2 es superconjunto de c3? : {c2 >= c3}")

print("\nVerificar la presencia de un elemento en el conjunto:")
print(f"¿2 está en c1? : {2 in c1}")
print(f"¿6 no está en c1? : {6 not in c1}")
