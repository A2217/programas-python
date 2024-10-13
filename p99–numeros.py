#ejercicio de conjuntos
A = {50, 60, 70, 80, 90, 100, 200}
B = {60, 90, 100, 300, 400, 500}
C = {10, 20, 60, 90, 70, 100, 600, 700}

print(f"Conjunto A: {A}")
print(f"Conjunto B: {B}")
print(f"Conjunto C: {C}")

union_AB = A | B
print(f"\nUnión de A y B: {union_AB}")

union_BC = B | C
print(f"Unión de B y C: {union_BC}")

diferencia_AC = A - C
print(f"Diferencia de A y C (A - C): {diferencia_AC}")

diferencia_simetrica_BC = B ^ C
print(f"Diferencia simétrica de B y C (B ^ C): {diferencia_simetrica_BC}")

interseccion_BC = B & C
print(f"Intersección de B y C: {interseccion_BC}")

print("\nComprobaciones:")

if A.issubset(B):
    print("A es subconjunto de B")
else:
    print("A NO es subconjunto de B")

if C.issubset(A):
    print("C es subconjunto de A")
else:
    print("C NO es subconjunto de A")

if 100 in A:
    print("100 está en A")
else:
    print("100 NO está en A")

if 60 in A and 60 in B and 60 in C:
    print("60 está en A, B y C")
else:
    print("60 NO está en A, B y C simultáneamente")

if 900 not in C:
    print("900 NO está en C")
else:
    print("900 está en C")
