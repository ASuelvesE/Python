# entities
from entities.Armario import *
# DAOS
from dao.DAOPrendasXML import DAOPrendasXML
# conexion
from dao.DAOPrendasMYSQL import *

DAOPrendas_MySQL = DAOPrendasMySQL()
DAOPrendas_XML = DAOPrendasXML()
armario = Armario()

def muestraTodo():
    armario = Armario()
    armario.lee() 
    DAOPrendas_XML.writeHTML(armario.prendas)
    DAOPrendas_XML.writeXML(armario.prendas,'./data/output.xml')
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
        DAOPrendas_XML.writeXML(elegidos,'./data/resultados.xml')
    
    elif elige == "Pantalon":
        for prenda in armario.prendas:
            if prenda.tipo == "pantalon":
                elegidos.append(prenda)
        DAOPrendas_XML.writeXML(elegidos,'./data/resultados.xml')

    elif elige == "Zapatilla":
        for prenda in armario.prendas:
            if prenda.tipo == "zapatillas":
                elegidos.append(prenda)
        DAOPrendas_XML.writeXML(elegidos,'./data/resultados.xml')

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
    DAOPrendas_XML.writeXML(armario.prendas,'./data/datos.xml') #Sobreescribo el xml con los datos del array de objetos
    menu()

def insertaPantalones():
    armario = Armario()
    armario.lee() 
    marca = input("\nDime la marca:")
    color = input("\nDime el color:")
    talla = input("\nDime la talla:")

    armario.prendas.append(Pantalon(marca,color,talla)) #añado una nuevo pantalon al array de objetos
    DAOPrendas_XML.writeXML(armario.prendas,'./data/datos.xml') #Sobreescribo el xml con los datos del array de objetos
    menu()

def insertaZapatillas():
    armario = Armario()
    armario.lee() 
    marca = input("\nDime la marca:")
    color = input("\nDime el color:")
    talla = input("\nDime la talla:")

    armario.prendas.append(Zapatillas(marca,color,talla)) #añado una nuevas zapatilla al array de objetos
    DAOPrendas_XML.writeXML(armario.prendas,'./data/datos.xml') #Sobreescribo el xml con los datos del array de objetos
    menu()

def borrarCamisetas():
    armario = Armario()
    armario.lee() 
    prendas = []
    for prenda in armario.prendas:#dame un array con los objetos que hay en datos.xml
        if prenda.tipo != "camiseta":
            prendas.append(prenda)
    DAOPrendas_XML.writeXML(prendas,'./data/datos.xml')
    print("Camisetas eliminadas de datos.xml")
    menu()

def borrarPantalones():
    armario = Armario()
    armario.lee() 
    prendas = []
    for prenda in armario.prendas:#dame un array con los objetos que hay en datos.xml
        if prenda.tipo != "pantalon":
            prendas.append(prenda)
    DAOPrendas_XML.writeXML(prendas,'./data/datos.xml')
    print("Pantalones eliminadas de datos.xml")
    menu()
    
def borrarZapatillas():
    armario = Armario()
    armario.lee() 
    prendas = []
    for prenda in armario.prendas:#dame un array con los objetos que hay en datos.xml
        if prenda.tipo != "zapatillas":
            prendas.append(prenda)
    DAOPrendas_XML.writeXML(prendas,'./data/datos.xml')
    print("Zapatillas eliminadas de datos.xml")
    menu()


def menu():
    print("___________________________________________________________________________________")
    print("\n\t---\tMENU:\t---")
    print("\nOpción A: Mostrar todas las prendas en formato HTML")
    print("Opción B: Mostrar las prendas especificadas en 'resultados.xml'")
    print("Opción C: Insertar una camiseta en datos.xml")
    print("Opción D: Insertar unos pantalones en datos.xml")
    print("Opción E: Insertar unas zapatillas en datos.xml")
    print("Opción F: Borrar las camisetas de datos.xml")
    print("Opción G: Borrar los pantalones de datos.xml")
    print("Opción H: Borrar las zapatillas de datos.xml\n")
    print("Opción I: Ver lo que hay en la BBDD")
    print("Opción J: Guardar en datos.xml lo que hay en la BBDD (Generar/Actualizar fichero)")
    print("Opción K: Insertar una prenda en la BBDD ")
    print("Opción L: Eliminar una prenda de la BBDD (Según atributos)")
    print("Opción M: Guardar en la BBDD lo que hay en datos.xml (Rellenar)\n")
    print("___________________________________________________________________________________")
    opcion = input("Elige una opcion de la 'A' a la 'M'\n")
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
    elif opcion == "I":
        DAOPrendas_MySQL.ver()
        menu()
    elif opcion == "J":
        DAOPrendas_XML.writeXML(DAOPrendas_MySQL.actualizarXML(),'./data/datos.xml')
        menu()  
    elif opcion == "K":
        DAOPrendas_MySQL.insertaBBDD()
        menu()  
    elif opcion == "L":
        DAOPrendas_MySQL.deleteBBDD()
        menu()  
    elif opcion == "M":
        DAOPrendas_MySQL.rellenarBBDD(armario.lee())
        menu()
    else:
         menu()

menu() 