def suma(n1, n2):
    s=n1+n2
    return s
print('\nSuma de dos numeros constantes: ')

print(suma(100,200))

r=suma(50,70)
print(f'\nLa suma r es {r}')

print('\nDame dos numeros: ')
a,b = int(input()), int(input())
print(f"La suma de los numeros es {suma(a,b)}")