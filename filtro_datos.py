import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
from scipy.signal import savgol_filter

# Cargar los datos

#data = pd.read_excel('G:\\dropbox\\Dropbox\\Ensayos Lab Res Mat\\27_09 Tesis y pruebas\\Ensayos tesis\\ensayo 1.xlsx')
#G:\\dropbox\\Dropbox\\Ensayos Lab Res Mat\\11_10  tesis\\Ensayo 1.xlsx
data = pd.read_excel('G:\\dropbox\\Dropbox\\Ensayos Lab Res Mat\\11_10  tesis\\ensayo 5.xlsx')


# Excluir la columna de tiempo y definir la columna de control
columnas_sensores = data.columns[1:-1]  # Esto excluye la primera columna (tiempo) y la última de control
columna_control = 'Celda de carga 100Ton'

# Parámetros del filtro de Savitzky-Golay
window_length = 15  # Aumentar la ventana del filtro
polyorder = 4  # Aumentar el orden del polinomio
alpha = 0.1  # Reducir el alpha para suavizar más

# Definir el umbral para detectar cambios drásticos
umbral = data[columna_control].diff().std() * 2  # Umbral basado en la desviación estándar de los cambios

# Crear nuevas columnas para los datos procesados y la tendencia segmentada
for sensor in columnas_sensores:
    # Filtrar con Savitzky-Golay
    datos_filtrados = savgol_filter(data[sensor], window_length=window_length, polyorder=polyorder)
    # Suavizar exponencialmente
    datos_suavizados = pd.Series(datos_filtrados).ewm(alpha=alpha).mean()
    
    # Agregar datos procesados a una nueva columna combinada
    data[f'{sensor}_Filtrado_Suavizado'] = datos_suavizados

# Identificar puntos de cambio en la columna de control
puntos_cambio = data[columna_control].diff().abs() > umbral  # Detecta cambios mayores al umbral

# Incluir el primer y el último índice como puntos de cambio
puntos_cambio.iloc[0] = True
puntos_cambio.iloc[-1] = True

# Crear nueva columna para almacenar la tendencia segmentada
for sensor in columnas_sensores:
    data[f'{sensor}_Tendencia_Segmentada'] = np.nan
    segmentos = np.where(puntos_cambio)[0]

    for i in range(len(segmentos) - 1):
        inicio = segmentos[i]
        fin = segmentos[i + 1]
        X_segmento = np.arange(fin - inicio).reshape(-1, 1)
        y_segmento = data[f'{sensor}_Filtrado_Suavizado'].iloc[inicio:fin].values.reshape(-1, 1)
        model = LinearRegression().fit(X_segmento, y_segmento)
        tendencia_segmentada = model.predict(X_segmento)
        data[f'{sensor}_Tendencia_Segmentada'].iloc[inicio:fin] = tendencia_segmentada.flatten()

# Filtrar, suavizar y combinar la columna de control
data[f'{columna_control}_Filtrado_Suavizado'] = savgol_filter(data[columna_control], window_length=window_length, polyorder=polyorder)
data[f'{columna_control}_Filtrado_Suavizado'] = pd.Series(data[f'{columna_control}_Filtrado_Suavizado']).ewm(alpha=alpha).mean()

# Guardar los datos procesados en un nuevo archivo
##data.to_excel('G:\\dropbox\\Dropbox\\Ensayos Lab Res Mat\\27_09 Tesis y pruebas\\Ensayos tesis\\ensayo 1 Analizado_completo.xlsx', index=False)
data.to_excel('G:\\dropbox\\Dropbox\\Ensayos Lab Res Mat\\11_10  tesis\\ensayo 5.xlsx', index=False)
