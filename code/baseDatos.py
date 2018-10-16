import mysql.connector

#Init
mydb=  mysql.connector.connect(
    host="HOST",
    user="USER",
    passwd="PASS",
    db="colaImpresionTfg",
    port="PORT"
)

mycursor = mydb.cursor(prepared=True)

#Utiles
def imprimeColumnas(nombre):
    mycursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = %s", (nombre,))
    for x in mycursor:
        print(x)

def imprimeTabla(nombre):
    mycursor.execute("SELECT * FROM "+nombre+" ;")
    for x in mycursor.fetchall():
        print(x)

def reiniciaTabla(nombre):
    mycursor.execute("DELETE FROM "+nombre+";")
    mycursor.execute("ALTER TABLE "+nombre+" AUTO_INCREMENT = 1")

def reiniciaBase():
    reiniciaTabla("Boquilla")
    reiniciaTabla("Pedido")
    reiniciaTabla("Trabajo")
    reiniciaTabla("Rollo")
    reiniciaTabla("Maquina")
    
#Inserts
def nuevaBoquilla(tamano):
    sql = "INSERT INTO Boquilla (Tamaño) VALUES (%s);"
    val=(tamano,)
    mycursor.execute(sql,val)
    mydb.commit()

def nuevoPedido(dueno,prioridad):
    sql = "INSERT INTO Pedido (Cliente,Prioridad) VALUES (%s,%s);"
    val = (dueno,prioridad)
    mycursor.execute(sql, val)
    mydb.commit()

def nuevoTrabajo(idPedido,idBoquilla,idRollo,idMaquina,volumen,Fecha):
    sql = "INSERT INTO Trabajo (Pedido_idPedido,Boquilla_idBoquilla,Rollo_idRollo,Maquina_idMaquina,volumen,Fecha_Entrega) VALUES (%s,%s,%s,%s,%s,%s);"
    val = (idPedido,idBoquilla,idRollo,idMaquina,volumen,Fecha)
    mycursor.execute(sql, val)
    mydb.commit()

def nuevoRollo(color,t_Impresion,peso):
    sql = "INSERT INTO Rollo (Color,T_Impresion,Peso) VALUES (%s,%s,%s);"
    val = (color,t_Impresion,peso)
    mycursor.execute(sql, val)
    mydb.commit()

def nuevaMaquina(idBoquilla,idRollo,estado):
    sql = "INSERT INTO Maquina (Boquilla_idBoquilla,Rollo_idRollo,Estado) VALUES (%s,%s,%s);"
    val = (idBoquilla, idRollo, estado)
    mycursor.execute(sql, val)
    mydb.commit()

#Delete
def borrarBoquilla(id):
    sql = "DELETE FROM Boquilla WHERE idBoquilla = %s"
    val = (id,)
    mycursor.execute(sql,val)
    mydb.commit()

def borrarPedido(id):
    sql = "DELETE FROM Pedido WHERE idPedido = %s"
    val = (id,)
    mycursor.execute(sql, val)
    mydb.commit()


def borrarTrabajo(id):
    sql = "DELETE FROM Trabajo WHERE idTrabajo = %s"
    val = (id,)
    mycursor.execute(sql,val)
    mydb.commit()

def borrarRollo(id):
    sql = "DELETE FROM Rollo WHERE idRollo = %s"
    val = (id,)
    mycursor.execute(sql,val)
    mydb.commit()

def borrarMaquina(id):
    sql = "DELETE FROM Rollo WHERE idRollo = %s"
    val = (id,)
    mycursor.execute(sql,val)
    mydb.commit()

