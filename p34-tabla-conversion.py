# Tabla de conversión de peso a dollar

print("Convierte n cantidad de pesos a dolares")

while(True):
    tc = 19.87
    while(True):
        ni = float(input("Valor inicial en pesos: "))
        nf = float(input("Valor final en pesos: "))    
        if ni < nf:
            break

    c = ni
    
    print("\nPesos\tDolar")
    print("-"*15)
    
    while c <= nf :
        print(f"{c}\t{c/tc:.2f}")
        c+=1
    print("-"*15)

    res=input('Deseas Continuar[S]/[N] ? ')
    if res.upper()=='N':
        print("Saliendo...")
        break