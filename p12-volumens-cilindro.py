#Calcula el volúmen de un cilindro

import math as mt

print("Ingresa las dimensiones del cilindro en centímetros\n")

radio =  int(input("radio :"))
altura = int(input("altura :"))

vol =  mt.pi*(radio**2)*altura

print(f"El volúmen del cilindro es: {vol} cm^3")