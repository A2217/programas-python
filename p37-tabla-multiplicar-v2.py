# Imprime las tablas de 1 a n, hasta m

while(True):
    n = int(input("De cuál número quieres imprimir su tabla de multiplicar?: "))
    m = int(input("Cuántas multiplicaciones quieres imprimir?:  "))
    t=1

    while t <= n:
        c=1
        print(f"\nTabla del {t} \n")

        while( c <= m ):
            print(f"{t} x {c} = {t*c}")
            c+=1
        t+=1
    r=input("\nDeseas Continuar [S]/[N]? ")
    if r.upper()=="N":
        print("Saliendo...")
        break