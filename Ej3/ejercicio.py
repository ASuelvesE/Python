from unittest import result


ficheroA = open("a.txt","r")
ficheroB = open("b.txt","r")

numero1 = int(ficheroA.read())
numero2 = int(ficheroB.read())

resultado = numero1 + numero2


suma = open("suma.txt","w")

suma.write(str(resultado))

ficheroA.close()
ficheroB.close()
suma.close()