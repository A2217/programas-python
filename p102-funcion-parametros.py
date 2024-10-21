def saluda(apaterno, nombre):
    print(f'Hola {apaterno} {nombre}')

    saluda('Juan','Perez') # Hola Juan Perez
    saluda('Juan') # genera error
    saluda('Juan','Perez','Diaz') # genera error