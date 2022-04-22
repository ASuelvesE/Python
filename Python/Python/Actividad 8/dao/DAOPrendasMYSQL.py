
from dao.DAOPrendas import DAOPrendas
from entities.Armario import *
from dao.DAOPrendasXML import *
from dao.DAOPrendasMYSQL import *
from bbdd.Bbdd import conexion

class DAOPrendasMySQL(DAOPrendas):

    def ver(self): #Imprime por consola las prendas que tenemos en la BBDD
        connect = conexion()
        mycursor = connect.cursor()
        mycursor.execute("SELECT id,tipo,marca,color,talla FROM prendas")
        myresult = mycursor.fetchall()

        print("PRENDAS: ")
        for prenda in myresult:
            aux = str(prenda[0])
            print("-Identificador: " + '{:2s}'.format(aux) + " -Tipo: " + prenda[1] + " -Marca: " + prenda[2] + " -Color: " + prenda[3] + " -Talla: " + prenda[4])

    def actualizarXML(self):
        connect = conexion()
        mycursor = connect.cursor()
        mycursor.execute("SELECT id,tipo,marca,color,talla FROM prendas")
        myresult = mycursor.fetchall()

        datos = []
        for prenda in myresult:
            if prenda[1] == "camiseta":
                datos.append(Camiseta(prenda[2],prenda[3],prenda[4])) #añado una nueva camiseta al array de objetos
            elif prenda[1] == "pantalon":
                datos.append(Pantalon(prenda[2],prenda[3],prenda[4])) #añado una nueva camiseta al array de objetos
            elif prenda[1] == "zapatillas":
                datos.append(Zapatillas(prenda[2],prenda[3],prenda[4])) #añado una nueva camiseta al array de objetos
        print("Datos actualizados en el fichero datos.xml")
        return datos

    def insertaBBDD(self):
        def insert(): #Funcion anidada, se ejecuta solo si se dan los datos correctamente
            connect = conexion()
            mycursor = connect.cursor()
            sql = "INSERT INTO prendas(tipo,marca,color,talla) VALUES (%s, %s, %s, %s)"
            val = (tipo,marca,color,talla)
            mycursor.execute(sql, val)
            connect.commit()
            print("Prenda insertada en la BBDD")
        print("Tenemos estos tipos de prendas: \n-Camiseta\n-Pantalon\n-Zapatilla")
        tipo = input("\nElige un tipo de prenda:\n")

        if tipo == "Camiseta":
            tipo = "camiseta"
            marca = input("\nDime la marca:")
            color = input("\nDime el color:")
            talla = input("\nDime la talla:")
            insert()
        elif tipo == "Pantalon":
            tipo = "pantalon"
            marca = input("\nDime la marca:")
            color = input("\nDime el color:")
            talla = input("\nDime la talla:")
            insert()
        elif tipo == "Zapatilla":
            tipo = "zapatillas"
            marca = input("\nDime la marca:")
            color = input("\nDime el color:")
            talla = input("\nDime la talla:")
            insert()
        else:
            print("\nNo tenemos esa prenda\n")

    def deleteBBDD(self):
        def delete():
            connect = conexion()
            mycursor = connect.cursor()
            sql = "DELETE FROM prendas WHERE id = %s"
            mycursor.execute(sql,val)
            connect.commit()
            print("Prenda eliminada de la BBDD")

        entrada = input("Dime el nº identificador de la prenda que quieres eliminar\n")
        con = conexion()
        mycursor = con.cursor()
        sql = "SELECT * FROM prendas WHERE id = %s"
        val = (str(entrada),)
        mycursor.execute(sql,val)
        resultado = mycursor.fetchall()

        for x in resultado: # Si devuelve algo... llama a delete()
            delete()

    def rellenarBBDD(self,prendas): #Actualiza la BBDD con las prendas que hay en datos.xml
        for prenda in prendas:
            tipo = prenda.tipo
            marca = prenda.marca
            color = prenda.color
            talla = prenda.talla

            connect = conexion()
            mycursor = connect.cursor()
            sql = "INSERT INTO prendas (tipo,marca,color,talla) VALUES (%s, %s, %s, %s)"
            val = (tipo,marca,color,talla)
            mycursor.execute(sql, val)
            connect.commit()
        print("Actualizada la BBDD")
        print("_________________________________________________________________\n")

