import mysql.connector

def conexion():    
    connect = mysql.connector.connect(
    #host="80.34.34.150",
    host="192.168.8.24",
    user="admin",
    password="angel",
    database="moviles"
    #port = "33069"
    )
    return connect

def ver():
    connect = conexion()
    mycursor = connect.cursor()

    mycursor.execute("SELECT * FROM catalogo")
    myresult = mycursor.fetchall()
    
    for x in myresult:
        print(x)

def insertar(id,modelo,precio,sistema,fabricante,pais):
    connect = conexion()
    mycursor = connect.cursor()

    sql = "INSERT INTO catalogo VALUES (%s, %s, %s, %s, %s, %s)"
    val = (id,modelo,precio,sistema,fabricante,pais)
    mycursor.execute(sql, val)

    connect.commit()
    print(fabricante + " " + modelo + " insertado en la BBDD")
    print("_________________________________________________________________\n")