import os
import datetime
import calendar

# Limpia la pantalla (compatible con Windows)
os.system('cls')

# Directorio actual
print(f'\nDirectorio actual: \n{os.getcwd()}')

# Listado de archivos en el directorio raíz
print('\nListado de archivos en el directorio raiz:')
os.chdir('C:/')  # Cambia al directorio raíz de Windows
print(os.listdir())

# Variables de entorno
print('\nVariables de entorno: ')
print(os.environ)

# Ruta de ejecución
print(f"\nRuta de ejecución: \n{os.getenv('PATH')}")

# Algunas funciones del módulo datetime
ahora = datetime.datetime.now()
print('\nLa fecha y hora actuales:', ahora)
print('\nLa fecha actual:', ahora.strftime('%b / %d / %Y'))
print('\nLa hora actual:', ahora.strftime('%H:%M'))

# Algunas funciones del módulo calendar
print('\nCalendario 2024: \n')
calendar.prcal(2024)
print('\nMes abril 2024: \n')
calendar.prmonth(2024, 4)
