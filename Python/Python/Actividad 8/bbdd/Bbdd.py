
import mysql.connector

def conexion():  
    try:  
        connect = mysql.connector.connect(
        #host="80.34.34.150",
        host="192.168.8.24",
        #host="127.0.0.1",
        database="armario",
        user="usuarioPrendas",
        #user="root",
        password="usuario_Prendas"
        #password=""
        #port = "33069"
        )
        return connect
    except mysql.connector.Error as e:
        print("Error al conectar con la BBDD", e)