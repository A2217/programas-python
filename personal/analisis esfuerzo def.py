import pandas as pd
import numpy as np

# Cargar los datos desde el archivo Excel
file_path = r'G:\Escritorio\datos filtrar\Datos ensayo 1.xlsx'
data = pd.read_excel(file_path)

# Verificar que las columnas existen
if not all(col in data.columns for col in ['carga', 'radial', 'axial']):
    raise KeyError("Las columnas 'carga', 'radial' y 'axial' deben estar presentes en los datos")

# Normalizar los datos para que comiencen desde cero
for col in ['carga', 'radial', 'axial']:
    data[col] = data[col] - data[col].min()

# Filtrar los datos para conservar solo los valores mayores
for col in ['carga', 'radial', 'axial']:
    filtrados = []
    ultimo_valor = -float('inf')  # Inicializar con un valor muy bajo
    for index, row in data.iterrows():
        if row[col] > ultimo_valor:
            filtrados.append(row)
            ultimo_valor = row[col]
    data = pd.DataFrame(filtrados)

# Transformar la columna 'carga' a 'esfuerzo'
diametro = 150  # 150 mm
area_transversal = np.pi * (diametro / 2)**2  # Área en mm²
data['esfuerzo'] = (data['carga'] * 9.81 * 1000) / area_transversal  # Esfuerzo en MPa

# Transformar las columnas 'radial' y 'axial' a deformaciones
data['deformacion_radial'] = data['radial'] / diametro  # Deformación (sin unidades)
data['deformacion_axial'] = data['axial'] / diametro  # Deformación (sin unidades)

# Calcular el módulo de elasticidad
carga_total_resistida = data['carga'].max()
carga_40 = 0.4 * carga_total_resistida
s2 = data['esfuerzo'][data['carga'] >= carga_40].iloc[0]
s1 = data['esfuerzo'][data['esfuerzo'] > 0.01].min()  # Usar un umbral para S1
e2 = data['deformacion_axial'][data['carga'] >= carga_40].iloc[0]
deformacion_radial_40 = data['deformacion_radial'][data['carga'] >= carga_40].iloc[0]
modulo_elasticidad = (s2 - s1) / (e2 - 0.00005)

# Imprimir resultados en el orden especificado
print(f"Esfuerzo Máximo (MPa): {data['esfuerzo'].max()}")
print(f"Esfuerzo al 40% de la carga total (S2): {s2} MPa")
print(f"Deformación Axial Máxima: {data['deformacion_axial'].max()}")
print(f"Deformación Radial Máxima: {data['deformacion_radial'].max()}")
print(f"Deformación Axial al 40% de la carga total (E2): {e2}")
print(f"Deformación Radial al 40% de la carga total: {deformacion_radial_40}")
print(f"Módulo de Elasticidad: {modulo_elasticidad} MPa")

# Guardar los datos transformados en un nuevo archivo Excel
output_path = r'G:\Escritorio\datos filtrar\datos_transformados.xlsx'
data.to_excel(output_path, index=False)
