from common.utils import read
from common.utils import write


def ejercicio1():
    print("Leyendo temperaturas y generando salidas")
    temperaturas = read('data/eltiempo.xml')
    # cabeceras HTML
    contentHTML = '<html>'
    contentHTML += '<body>'
    # recorro las temperaturas
    for lectura in temperaturas:
        elementoHora = lectura.find('hora').tag
        elementoHoraText = lectura.find('hora').text
        elementoGrados = lectura.find('grados').tag
        elementoGradosText = lectura.find('grados').text
        # item en HTML
        contentHTML += '<p>' + elementoHora + ': ' + elementoHoraText + '</p>'
        contentHTML += '<p>' + elementoGrados + ': ' + elementoGradosText + '</p>'
    # cierro el HTML
    contentHTML += '</body>'
    contentHTML += '</html>'
    # escribo en ficheros el contenido formado arriba
    write("temperaturas.html", contentHTML)


def ejercicio2():
    print("Leyendo datos del concesionario")
    print("¿Qué coches quieres ver?")
    kmMaximos = int(input("nº máximo de km: "))
    marca = input("Marca: ")
    coches = read('data/concesionario.xml')
    # procesar los vehículos y exportar a HTML
    contentHTML = "<html>"
    contentHTML += "<body>"

    for coche in coches:
        if int(coche.attrib["km"]) < kmMaximos and coche.attrib["marca"] == marca:
            contentHTML += '<p>' +"Matrícula: " + coche.attrib["matricula"] + " Marca: " + marca + " Modelo: " + coche.attrib["modelo"] + " KM: " + coche.attrib["km"] + '</p>'
    contentHTML += '</body>'
    contentHTML += '</html>'
    write("concesionario.html", contentHTML)


def ejercicio3():
    print("Leyendo estudiantes")
    print("¿Qué estudiantes quieres buscar?")
    nombre = input("Nombre: ")
    modulo = input("Algún módulo que curse: ")
    # procesar los estudiantes y exportar a HTML
    alumnos = read('data/estudiantes.xml')
    contentHTML = "<html>"
    contentHTML += "<body>"

    for alumno in alumnos:
        if alumno.attrib["nombre"] == nombre:
            contentHTML += '<p>' +"Nombre: " + nombre + '</p>'

            asignaturas = alumno.find("asignaturas")
            asignatura = asignaturas.find("asignatura")

            if asignatura.attrib["nombre"] == modulo:
                for asignatura in asignaturas:
                    contentHTML += '<p>' +" Asignatura: " + asignatura.attrib["nombre"] + '</p>'

    contentHTML += '</body>'
    contentHTML += '</html>'
    write("estudiantes.html", contentHTML)


def ejercicio4():
    print("Leyendo productos")
    print("¿Qué productos quieres buscar?")
    nombre = input("Nombre: ")
    mayorMenor = input("Superiores a un precio (si|no): ")
    precio = int(input("Precio: "))
    # procesar los productos y exportar a HTML
    productos = read("data/productos.xml")
    contentHTML = "<html>"
    contentHTML += "<body>"

    for producto in productos:
        if producto.attrib["nombre"] == nombre:
            if int(producto.attrib["precio"]) > precio and mayorMenor == "si":
                contentHTML+= '<p>' "Nombre : " + nombre + " Precio: " + str(precio)

            if int(producto.attrib["precio"]) < precio and mayorMenor == "no":
                contentHTML+= '<p>' "Nombre : " + nombre + " Precio: " + str(precio)

    contentHTML += '</p>'
    contentHTML += '</body>'
    contentHTML += '</html>'
    write("productos.html", contentHTML)

def main():
    ejercicio = int(input("nº de ejercicio: "))
    if ejercicio == 1:
        ejercicio1()
    elif ejercicio == 2:
        ejercicio2()
    elif ejercicio == 3:
        ejercicio3()
    elif ejercicio == 4:
        ejercicio4()


main()
