from utils import read
from clases.Movil import Movil
from clases.Fabricante import Fabricante
from conexion.interlazar import *



arrayMoviles = []

f = open('datos/moviles.xml') 
moviles = read(f) #lee y crea un array
for movil in moviles:
    id = movil.attrib["id"]
    modelo = movil.attrib["modelo"]
    precio = movil.attrib["precio"]
    so = movil.attrib["SO"]

    fabricante = movil.find("fabricante")
    nombre = fabricante.attrib["nombre"]
    pais = fabricante.attrib["pais"]

    arrayMoviles.append(Movil(id,modelo,precio,so,Fabricante(nombre,pais)))


for a in arrayMoviles:
    print("Id: "+ a.id+"\nModelo: "+ a.modelo+"\nPrecio: "+ a.precio+"\nSO: "+ a.so+"\nNombre del fabricante: " + a.fabricante.nombre+"\nPais del fabricante: " + a.fabricante.pais+"\n")
    insertar(a.id,a.modelo,a.precio,a.so,a.fabricante.nombre,a.fabricante.pais)

def menu():
    print("Opcion : A ==> Ver las Móviles que hay en la base de datos\n Opcion : B ==> Insertar en la BBDD los moviles que hay en el xml")
    opcion = input("Elige una opcion")
    