#Dada una lista de numeros, regresar los apres

def pares(lista):
    p=[]
    for n in lista:
        if n % 2 == 0:
            p.append(n)
    return p

nums = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
print(nums)
res = pares(nums)
print(res)