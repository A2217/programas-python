# dada uan lista de numeros introducida por el usuario, regresar el mayor y el menor

def leerdatos():
    datos=[]
    while True:
        d = int(input('Ingresa numero: '))
        if d==-1:break
        datos.append(d)
    return datos

def mayor(lista):
    m = lista[0]
    for n in lista:
        if n > m:
            m = n
    return m

def menor(lista):
    m = lista[0]
    for n in lista:
        if n < m:
            m = n
    return m

#programa principal
datos = leerdatos()
print(datos)
may = mayor(datos)
men = menor(datos)
print ('el mayor es ',may)
print ('el menor es ',men)