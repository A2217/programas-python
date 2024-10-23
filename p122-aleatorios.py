def generar_aleatorios(n):
    import random
    lista = []
    for i in range(n):
        lista.append(random.randint(1, 100))
    return lista

def suma_lista(lista1, lista2):
    lista3 = []
    n = len(lista1)  
    for i in range(n):
        lista3.append(lista1[i] + lista2[i])  
    return lista3

# programa principal
MAX = 20

nums1 = generar_aleatorios(MAX)
nums2 = generar_aleatorios(MAX)
nums3 = suma_lista(nums1, nums2)

print('Lista 1: ', nums1)
print('Lista 2: ', nums2)
print('Lista 3 (suma): ', nums3)
