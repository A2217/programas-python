import pandas as pd

# Ruta del archivo
file_path = r'D:\Dropbox\Ensayos Lab Res Mat\Nueva carpeta\datos filtrar\Datos transformados.xlsx'

# Cargar los datos desde el archivo Excel
data = pd.read_excel(file_path)

# Verificar que las columnas existen
required_columns = ['esfuerzo', 'deformacion_radial', 'deformacion_axial']
if not all(col in data.columns for col in required_columns):
    raise KeyError(f"El archivo debe contener las columnas: {', '.join(required_columns)}")

# Obtener el esfuerzo máximo y al 40%
esfuerzo_maximo = data['esfuerzo'].max()
esfuerzo_40 = 0.4 * esfuerzo_maximo

# Obtener las deformaciones al 100% y al 40% del esfuerzo
deformacion_axial_max = data['deformacion_axial'][data['esfuerzo'] == esfuerzo_maximo].values[0]
deformacion_radial_max = data['deformacion_radial'][data['esfuerzo'] == esfuerzo_maximo].values[0]

deformacion_axial_40 = data['deformacion_axial'][data['esfuerzo'] >= esfuerzo_40].iloc[0]
deformacion_radial_40 = data['deformacion_radial'][data['esfuerzo'] >= esfuerzo_40].iloc[0]

# Calcular el módulo de elasticidad
s2 = esfuerzo_40
s1 = data['esfuerzo'][data['esfuerzo'] > 0].min()
e2 = deformacion_axial_40
modulo_elasticidad = (s2 - s1) / (e2 - 0.00005)

# Escribir los resultados en un archivo .txt
output_file_path = r'D:\Dropbox\Ensayos Lab Res Mat\Nueva carpeta\datos filtrar\resultados.txt'
with open(output_file_path, 'w') as file:
    file.write(f"Esfuerzo Máximo (MPa): {esfuerzo_maximo}\n")
    file.write(f"Esfuerzo al 40% (MPa): {esfuerzo_40}\n")
    file.write(f"Deformación Axial Máxima: {deformacion_axial_max}\n")
    file.write(f"Deformación Radial Máxima: {deformacion_radial_max}\n")
    file.write(f"Deformación Axial al 40%: {deformacion_axial_40}\n")
    file.write(f"Deformación Radial al 40%: {deformacion_radial_40}\n")
    file.write(f"Módulo de Elasticidad (MPa): {modulo_elasticidad}\n")

print(f"Resultados guardados en {output_file_path}")
