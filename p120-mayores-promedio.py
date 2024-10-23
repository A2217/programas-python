#Calcula el promedio de una lista pero regresa los que son mayores al promedio
def leerdatos():
    datos=[]
    while True:
        d = int(input('Ingresa numero: '))
        if d==-1:break
        datos.append(d)
    return datos

def promedio(nums):
    s = 0
    for n in nums:
        s += n
    return s / len(nums)

def mayoresprom(nums, prom):
    mp = []
    for n in nums:
        if n > prom:
            mp.append(n)
    return mp

#programa principal

nums = leerdatos()
print(nums)

prom = promedio(nums)
mayprom = mayoresprom(nums,prom)
print('Promedio: ', prom)
print('Numeros mayores al promedio: ',mayprom)

