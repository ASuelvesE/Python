
fichero = open("fichero.txt","w")

for numero in range(0,10):
    if(numero%2 != 0):
        print(numero)
        fichero.write((str)(numero))
fichero.close()
