# Uso de las funciones trigonométricas en python

import math

print('Cálculo de las funciones trigonométricas')
print('Dame un ángulo')

angulo = int(input())
seno = math.sin(angulo)
coseno = math.cos(angulo)
tangente = math.tan(angulo)
grados = math.degrees(angulo)

salida = ('Resumen de funciones\n'
          f'El seno es {seno}\n'
          f'El coseno es {coseno}\n'
          f'La tangente es {tangente}\n'
          f'El ángulo {angulo} en radianes equivale a {grados}\n')

print(salida)