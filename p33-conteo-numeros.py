# Cuenta números, los suma, cuenta positivos, negativos y ceros, parar con 999

cuenta = num = suma = 0
cuenta_positivos = cuenta_negativos = cuenta_ceros=0

print("Cuenta números, los suma, cuenta positivos, negativos y ceros, parar con 999\n")

while(True):
    num = int(input("Ingresa un número "))
    if num != 999:
        cuenta += 1
        suma += num
        if num > 0:
            cuenta_positivos += 1
        elif num <0 :
            cuenta_negativos += 1
        else:
            cuenta_ceros += 1
    else:
        break

print(f'Se introdujeron {cuenta} numeros')
print('Positivos: ', cuenta_positivos)
print('Negativos: ', cuenta_negativos )
print('Ceros : ', cuenta_ceros)
print('La suma de los numeros es', suma)