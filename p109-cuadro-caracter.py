# cuadro de r x c de un carácter
def cuadro_caracter(r, c, car):
    for i in range(1, r+1):
        for j in range(1, c+1):
            print(car, end=' ')
        print('\r')

r = int(input('Cuantos renglones? '))
c = int(input('Cuantas columnas? '))
car = input('Cual caracter? ')
cuadro_caracter(r, c, car)