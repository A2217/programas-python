#Calcula la hipotenusa de un tríangulo

import math as mt

l1 = int(input("Ingresa la longitud del cateto adyacente: "))
l2 = int(input("Ingresa la longitud del cateto opuesto: "))

hip=mt.sqrt(mt.pow(l1,2)+mt.pow(l2,2))

print(f"La hipotenusa del triangulo es: {hip:.2f}")
