import pandas as pd
import numpy as np

# Cargar el archivo Excel
file_path = "G:/Escritorio/datos a escalar.xlsx"
data = pd.read_excel(file_path)

# Asumimos que los datos a escalar están en las columnas 1 y 2 (A y B)
# y que las columnas de referencia están en las columnas 3 y 4 (C y D)
ref_data = data.iloc[:, 0:2].values  # Primeras dos columnas (A y B)
data_to_scale = data.iloc[:, 2:4].values  # Siguientes dos columnas (C y D)

# Ajustar un polinomio a los datos de referencia
degree = 3  # Puedes cambiar el grado del polinomio según sea necesario
coeffs = np.polyfit(ref_data[:, 0], ref_data[:, 1], degree)

# Crear una función polinómica a partir de los coeficientes
poly_func = np.poly1d(coeffs)

# Escalar los datos utilizando la función polinómica
scaled_data = []

for row in data_to_scale:
    scaled_row = poly_func(row)
    scaled_data.append(scaled_row)

# Convertir a un DataFrame
scaled_df = pd.DataFrame(scaled_data, columns=["Scaled_Data_1", "Scaled_Data_2"])

# Agregar los datos escalados al DataFrame original
result_df = pd.concat([data, scaled_df], axis=1)

# Guardar los resultados en un nuevo archivo Excel
output_path = "G:/Escritorio/datos_escalados.xlsx"
result_df.to_excel(output_path, index=False)

print("El archivo de datos escalados ha sido guardado en:", output_path)
