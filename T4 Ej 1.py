aprobado=0
suspeso=0
for x in range(10)
         nota=int(input("Introduce una nota",x))
         if (nota<5):
             suspenso=suspenso+1
         else:
             aprobado=aprobado+1
print("aprobabo:",aprobado)
print("suspenso:",suspenso)
