# Dado un número entero base y un exponente exp, calcular la potencia de base elevado a exp

print("Imprime un número elevado a uan potencia")
base = int(input("Base: "))
exp = int(input("Exponente: "))
p = 1

for _ in range(exp):
    p *= base

print(f"{base} ^ {exp} = {p}" )