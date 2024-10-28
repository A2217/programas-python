# Código de clase
class Empleado:
    def __init__(self, nombre, edad, sexo, casado):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.casado = casado
    
    def __str__(self):
        return f'Nombre: {self.nombre}, Edad: {self.edad}, Sexo: {"Mujer" if self.sexo == "M" else "Hombre"}, Casado: {"Casado" if self.casado else "No Casado"}'

# Programa principal
import os
os.system('cls')

emp1 = Empleado('Jose Diaz', 35, 'H', True)
print('Nombre: ', emp1.nombre)
print('Edad : ', emp1.edad)
print('Sexo : ', emp1.sexo)
print('Casado: ', emp1.casado)
print(emp1)

emp2 = Empleado('Rocio Espinoza', 15, 'M', False)
print('Nombre: ', emp2.nombre)
print('Edad : ', emp2.edad)
print('Sexo : ', emp2.sexo)
print('Casado: ', emp2.casado)
print(emp2)

emp3 = Empleado('Rebeca Soto', 22, 'M', True)
print('Nombre: ', emp3.nombre)
print('Edad : ', emp3.edad)
print('Sexo : ', emp3.sexo)
print('Casado: ', emp3.casado)
print(emp3)

# Cálculo del promedio de edad
pedad = (emp1.edad + emp2.edad + emp3.edad) / 3
print(f'El promedio de la edad de los empleados es {pedad:.2f}')
