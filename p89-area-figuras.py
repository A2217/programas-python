# Calcular el área de algunas figuras geométricas

import math

figuras = {
    "Circulo": {"radio": 0, "formula": "math.pi * r ** 2"},
    "Triangulo": {"base": 0, "altura": 0, "formula": "0.5 * b * a"},
    "Rectangulo": {"largo": 0, "ancho": 0, "formula": "l * a"}
}

print("Calculadora de áreas de figuras geométricas")

for k, v in figuras.items():
    print(f'{k:<10} - {v["formula"]}')

while True:
    fig = input("Figura: ").title()
    if fig in figuras: 
        break

area = 0
if fig == "Circulo":
    r = int(input("Radio: "))
    area = eval(figuras[fig]["formula"].replace("r", str(r)))

elif fig == "Triangulo":
    b = int(input("Base: "))
    a = int(input("Altura: "))
    area = eval(figuras[fig]["formula"].replace("b", str(b)).replace("a", str(a)))

elif fig == "Rectangulo":
    l = int(input("Largo: "))
    a = int(input("Ancho: "))
    area = eval(figuras[fig]["formula"].replace("l", str(l)).replace("a", str(a)))

print(f"Área: {area:.2f}")
