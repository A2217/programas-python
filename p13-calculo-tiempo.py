#calcula el quivalente del tiempo en días, minutos y segundos

h=int(input("Ingresa la cantidad de horas que quieres saber su equivalente en días, minutos y segundos: "))

d = h/24
m = h*60
s = m*h

salida = (f'{h} horas equivale a: \n'
          f'{d:.2f} días\n'
          f'{m} minutos\n'
          f'{s} segundos\n'
         )

print(salida)