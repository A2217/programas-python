# Uso de las funciones trigonométricas en python

import math as mt

print('Cálculo de las funciones trigonométricas sobre un ángulo')
print('Dame un ángulo')

angulo = int(input())
angulor = mt.radians(angulo)
seno = mt.sin(angulo)
coseno = mt.cos(angulo)
tangente = mt.tan(angulo)
grados = mt.degrees(angulo)

salida = ('Resumen de funciones\n'
          f'El ángulo en radianes es {angulor}\n'
          #f'El seno es {seno}\n'
          f"El seno es {mt.sin(angulor):.3f}"
          f'El coseno es {coseno}\n'
          f'La tangente es {tangente}\n'
          f'El ángulo {angulo} en radianes equivale a {grados}\n')

print(salida)
