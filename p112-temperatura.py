# Temperaturas
def fahrenheit(temp):
    return ( temp * (9/5) ) +32

def centigrados(temp):
    return ( temp-32 ) * (5/9)
print('[1] Convertir a Fahrenheit')
print('[2] Convertir a Centigrados')
op = int(input("Elige una opcion: "))
if op==1 :
    temp = int(input('Dame una temperatura en Centigrados? '))
    print(f'La temperatura en grados Fahrenheit es {fahrenheit(temp)}')
elif op==2:
    temp = int(input('Dame una temperatura en Fahrenheit? '))
    print(f'La temperatura en grados Centigrados es {centigrados(temp)}')