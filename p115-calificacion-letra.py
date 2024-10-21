# Calificación con letra

def califletra(cal):
    if cal>=90 and cal<=100:
        return 'A', 'Excelente'
    elif cal>=80 and cal<90:
        return 'B', 'Bien'
    elif cal>=70 and cal<80:
        return 'C', 'Suficiente'
    elif cal>=60 and cal<70:
        return 'D', 'Deficiente'
    elif cal>=0 and cal<60:
        return 'F', 'Reprobado'

calificacion = int(input('Dame una calificacion entre 1 y 100: '))
letra , mensaje = califletra(calificacion)
print(f'Tu calificacion de {calificacion} corresponde a {letra} y esta {mensaje}')