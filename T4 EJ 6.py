Lista1=0
Lista2=0
for x in range(5):
    num1=int(input("Introduce un numero de la lista 1:"))
    Lista1=Lista1+num1

for x in range(5):
     num2=int(input("Introduce un numero de la lista 2:"))
     Lista2=Lista2+num2

if (Lista1>Lista2):
    print("Lista 1 mayor")
else:
    if(Lista2>Lista1):
        print("Lista 2 mayor")
    else:
        print("Listas iguales")
