pares=0
impares=0
n=int(input("Introduce el numero de elementos a leer"))
for x in range(n):
    num=int(input("Introduce un numero:"))
    if (num%2==0):
        pares=pares+1
    else:
        impares=impares+1
print("pares:",pares)
print("impares:",impares)
