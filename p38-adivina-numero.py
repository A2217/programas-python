# El usuario adivina un número entre 1 y 100

import random, os

num_sec = random.randint(1, 100)
intentos = 0

while(True):

    while True:
        n = int(input("Adivine el número secreto entre [1-100]: "))
        intentos += 1

        if n == num_sec:

            print(f"\nFelicidades! Adivinaste el número en {intentos} intentos.")
            intentos = 0
            break

        elif n < num_sec:
            print("El número es mayor.")

        else:
            print("El número es menor.")

    if not input("\nQuieres continuar? [S]/[N]: ").upper().startswith("S"): 
        print("Saliendo...")
        break