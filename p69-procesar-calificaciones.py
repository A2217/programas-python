# Procesar calificaciones

print("Se procesarán las calificaciones \n")
print("Introduce calificaciones entrer 0 y 10 (Ingresa -1 para terminar de ingresar):\n")
nums=[]
n=suma=prom=0
while n!=-1:
    n = float(input("Numero: "))
    if n>=0 and n<=10:
        nums.append(n)
        suma+=n
    else:
        print("x")

print("< fin")
prom=suma/len(nums)
mp=[]
for n in nums:
    if n>prom:
        mp.append(n)

print(f"\nCapturaste {len(nums)} números")
print(f"Las numeros son: {nums}")
print("\nEstadisticas: ")
print(f"Suma: {suma}")
print(f"Promedio: {prom}")
print(f"Mayores promedio: {len(mp)} : {mp}")
print(f"Mayor: {max(nums)}")