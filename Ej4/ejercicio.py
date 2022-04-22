
class Persona:
    nombre = ""
    fechaNacimiento = ""
    estatura = 0

angel = Persona()

angel.nombre = input("Introduce un nombre\n")
angel.fechaNacimiento = input("Introduce una fecha de nacimiento\n")
angel.estatura = input("Introduce una estatura\n")

ficheroA = open(angel.nombre + ".txt","w")
ficheroA.write(angel.nombre + "\n" + angel.fechaNacimiento + "\n" + angel.estatura)
ficheroA.close()