divisor=1
n=int(input("Ingrese un número:"))
while divisor<=n:
    resto=n % divisor
    if resto == 0:
        print(divisor)
    divisor = divisor + 1
