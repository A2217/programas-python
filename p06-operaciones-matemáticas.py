# Operaciones matemáticas

#x = 10.5
#y = 2.5

x=float(input("Dame el primer valor ?"))
y=float(input("Dame el segundo valor ?"))

suma = x + y
resta = x - y
mult = x * y
div = x / y
res = x % y
exp = x ** y
dive = x // y

print(f'suma {suma}\nresta {resta}\nmultiplicación {mult}\ndivision {div}')
print(f'residuo {res}\nexponenciación {exp:.2f}\ndivision entera {dive}')
