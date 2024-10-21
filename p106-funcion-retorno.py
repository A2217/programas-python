def suma(n1, n2):
    return n1 + n2
print('\nSuma de dos numeros constantes: ')
print(suma(100,200))

print('Dame dos numeros: ')
a,b = int(input()), int(input())
print(f"La suma de los numeros es {suma(a,b)}")