#Union de conjuntos
A = {"Juan", "Maria", "Pedro", "Jose", "Rocio"}
B = {"Pedro", "Juan", "Pablo", "Mateo", "Esther"}

print(f"\nConjunto A: {A}")
print(f"Conjunto B: {B}")

union = A | B
print(f"\nUnión de A y B: {union}")

interseccion = A & B
print(f"\nIntersección de A y B: {interseccion}")

diferencia = A - B
print(f"\nDiferencia de A y B (A - B): {diferencia}")

diferencia_simetrica = A ^ B
print(f"\nDiferencia simétrica de A y B: {diferencia_simetrica}")

C = {"Pablo", "Mateo"}

if C.issubset(B):
    print(f"\nEl conjunto {{'Pablo', 'Mateo'}} es subconjunto de B")
else:
    print(f"\nEl conjunto {{'Pablo', 'Mateo'}} NO es subconjunto de B")

D = {"Reynaldo", "Angelica"}

if A.issuperset(D):
    print(f"\nEl conjunto A es superconjunto de {{'Reynaldo', 'Angelica'}}.")
else:
    print(f"\nEl conjunto A NO es superconjunto de {{'Reynaldo', 'Angelica'}}.")

if "Pedro" in A:
    print("\nPedro está en A")
else:
    print("\nPedro NO está en A")

if "Lilia" not in B:
    print("\nLilia no está en B")
else:
    print("\nLilia está en B")