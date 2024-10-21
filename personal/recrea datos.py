import pandas as pd
import numpy as np
from numpy.polynomial.polynomial import Polynomial

# Ruta del archivo
file_path = r'G:\Escritorio\datos filtrar\este.xlsx'

# Cargar los datos desde el archivo Excel
data = pd.read_excel(file_path)

# Verificar que la primera columna existe
if data.shape[1] < 1:
    raise KeyError("El archivo debe tener al menos una columna")

# Analizar la primera columna
x = np.arange(len(data))
y = data.iloc[:, 0]

# Ajustar un polinomio de grado 5 a los datos no nulos y no ceros
mask = y != 0
if len(y[mask]) < 6:
    raise ValueError("No hay suficientes datos no nulos para ajustar un polinomio de grado 5")

p = Polynomial.fit(x[mask], y[mask], 6)

# Rellenar los valores 0 utilizando el polinomio, excepto el primer dato
data.iloc[1:, 0] = np.where(data.iloc[1:, 0] == 0, p(x[1:]), data.iloc[1:, 0])

# Asegurar que el primer dato sea 0
data.iloc[0, 0] = 0

# Verificar los datos finales
print("Datos finales:")
print(data.head())

# Guardar los datos completados en un nuevo archivo Excel
output_path = r'G:\Escritorio\datos filtrar\datos_completados_polinomio_v2.xlsx'
data.to_excel(output_path, index=False)

print(f"Datos completados y guardados en {output_path}")
