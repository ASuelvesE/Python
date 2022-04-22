import random

aleatorio = random.randrange(1, 26)
print(aleatorio)

print("Acierta el numero del 0 al 25\n")
i=0
while  i<10:
    numero = int(input("\nEscribe un numero\n"))
    if aleatorio == numero:
        print("Acertaste!!")
        break
    i+=1
print("Se acabaron los intentos")