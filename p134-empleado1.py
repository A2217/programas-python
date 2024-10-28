# Código de clase
class Empleado:
    def __init__(self, nombre, edad):
        self.nombre  = nombre
        self.edad    = edad
    
    def __str__(self):
        return f'Nombre: {self.nombre}, Edad: {self.edad}'

# Programa principal
import os
os.system('cls')

emp1 = Empleado('Jose Diaz', 35)
emp2 = Empleado('Juan Perez', 66)

print('\Datos del empleado 1')
print(f'Nombre empleado: {emp1.nombre}')
print(f'Edad empleado:   {emp1.edad} ') 
print(f'Empleado: {emp1}')
emp1.edad = 40
print(f'Empleado: {emp1}')

print('\Datos del empleado 2')
print(f'Nombre empleado: {emp2.nombre}')
print(f'Edad empleado:   {emp2.edad} ') 
print(f'Empleado: {emp2}')
