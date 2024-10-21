# Numero mayor
def mayor(c1,c2,c3):
    if c1>c2 and c1>c3:
        may = c1
    elif c2>c1 and c2>c3:
        may = c2
    else:
        may = c3
    return may
    
print("Dame 3 calificaciones")
a,b,c = float(input()), float(input()), float(input())
print(f"la calificacion mayor es: {mayor(a,b,c)}")