#Conversión de temperaturas de centigrados a Fahrenheit

print("Conversión de temperaturas de centigrados a Fahrenheit \n")
opcion = str.upper( input('Convertir a [C]entigrados o convertir a [F]ahrenheit') )

if opcion == 'C':
    print("\nConvirtiendo a Centigrados\n")
    t = float(input("Ingresa los grados Fahrenheit: "))
    r = (t - 32) * 5 / 9
    print(f'{t}° Fahrenheit, equivalen a {r:.2f}° Centigrados')
else :
    print("\nConviritiendo a Fahrenheit\n")
    t = float(input("Ingresa los grados Centigrados"))
    r = ( t * 9 / 5 ) + 32
    print(f"{t}° Fahrenheit, equivalen a {r:.2f}° Centigrados")