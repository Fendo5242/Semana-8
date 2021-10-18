cont=0
div=0
n=int(input("Ingrese un número:"))
while div<=n:
    div+=1
    if n % div == 0:
        cont+=1
if cont==2:
    print("El número es primo")
else:
    print("El número es no primo")
