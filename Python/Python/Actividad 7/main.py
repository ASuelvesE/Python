# entities
from entities.Armario import *
# controllers
from controller.output import writeHTML
from controller.output import writeXML



def muestraTodo():
    armario = Armario()
    armario.lee() 
    writeHTML(armario.prendas)
    writeXML(armario.prendas,'./data/output.xml')
    menu()

def muestraPrendas():
    armario = Armario()
    armario.lee() 
    print("Tenemos estos tipos de prendas: \n-Camiseta\n-Pantalon\n-Zapatilla")
    elige = input("\nElige un tipo de prenda:\n")

    elegidos = []

    if elige == "Camiseta":
        for prenda in armario.prendas:
            if prenda.tipo == "camiseta":
                elegidos.append(prenda)
        writeXML(elegidos,'./data/resultados.xml')
    
    elif elige == "Pantalon":
        for prenda in armario.prendas:
            if prenda.tipo == "pantalon":
                elegidos.append(prenda)
        writeXML(elegidos,'./data/resultados.xml')

    elif elige == "Zapatilla":
        for prenda in armario.prendas:
            if prenda.tipo == "zapatillas":
                elegidos.append(prenda)
        writeXML(elegidos,'./data/resultados.xml')

    else:
        print("\nNo tenemos esa prenda\n")
        muestraPrendas() 

    menu()

def insertaCamiseta():
    armario = Armario()
    armario.lee() 
    marca = input("\nDime la marca:")
    color = input("\nDime el color:")
    talla = input("\nDime la talla:")

    armario.prendas.append(Camiseta(marca,color,talla)) #añado una nueva camiseta al array de objetos
    writeXML(armario.prendas,'./data/datos.xml') #Sobreescribo el xml con los datos del array de objetos
    menu()

def insertaPantalones():
    armario = Armario()
    armario.lee() 
    marca = input("\nDime la marca:")
    color = input("\nDime el color:")
    talla = input("\nDime la talla:")

    armario.prendas.append(Pantalon(marca,color,talla)) #añado una nueva camiseta al array de objetos
    writeXML(armario.prendas,'./data/datos.xml') #Sobreescribo el xml con los datos del array de objetos
    menu()

def insertaZapatillas():
    armario = Armario()
    armario.lee() 
    marca = input("\nDime la marca:")
    color = input("\nDime el color:")
    talla = input("\nDime la talla:")

    armario.prendas.append(Zapatillas(marca,color,talla)) #añado una nueva camiseta al array de objetos
    writeXML(armario.prendas,'./data/datos.xml') #Sobreescribo el xml con los datos del array de objetos
    menu()

def borrarCamisetas():
    armario = Armario()
    armario.lee() 
    prendas = []
    for prenda in armario.prendas:#dame un array con los objetos que hay en datos.xml
        if prenda.tipo != "camiseta":
            prendas.append(prenda)
    writeXML(prendas,'./data/datos.xml')
    print("Camisetas eliminadas de datos.xml")
    menu()

def borrarPantalones():
    armario = Armario()
    armario.lee() 
    prendas = []
    for prenda in armario.prendas:#dame un array con los objetos que hay en datos.xml
        if prenda.tipo != "pantalon":
            prendas.append(prenda)
    writeXML(prendas,'./data/datos.xml')
    print("Pantalones eliminadas de datos.xml")
    menu()
    
def borrarZapatillas():
    armario = Armario()
    armario.lee() 
    prendas = []
    for prenda in armario.prendas:#dame un array con los objetos que hay en datos.xml
        if prenda.tipo != "zapatillas":
            prendas.append(prenda)
    writeXML(prendas,'./data/datos.xml')
    print("Zapatillas eliminadas de datos.xml")
    menu()


def menu():
    print("\n\t---\tMENU:\t---")
    print("\nOpción A: Mostrar todas las prendas en formato HTML")
    print("Opción B: Mostrar las prendas especificadas en 'resultados.xml'")
    print("Opción C: Insertar una camiseta")
    print("Opción D: Insertar unos pantalones")
    print("Opción E: Insertar unas zapatillas")
    print("Opción F: Borrar las camisetas")
    print("Opción G: Borrar los pantalones")
    print("Opción H: Borrar las zapatillas\n")
    opcion = input("Elige una opcion de la 'A' a la 'H'\n")
    if opcion == "A":
        muestraTodo()
    elif opcion == "B":
        muestraPrendas()
    elif opcion == "C":
        insertaCamiseta()
    elif opcion == "D":
        insertaPantalones()
    elif opcion == "E":
        insertaZapatillas()
    elif opcion == "F":
        borrarCamisetas()
    elif opcion == "G":
        borrarPantalones()
    elif opcion == "H":
        borrarZapatillas()
    else:
         menu()

menu() 