cont=1
i=int(input("Ingrese un número "))
if i>0:
    while cont <= 12:
        tabla=cont*i
        print(cont,"x",i,"=",tabla)
        cont += 1       
else:
    print("Error")
    