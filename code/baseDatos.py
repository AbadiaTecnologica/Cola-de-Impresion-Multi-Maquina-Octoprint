import mysql.connector
mydb=  mysql.connector.connect(
    host="HOST",
    user="USER",
    passwd="PASS",
    db="colaImpresionTfg",
    port="PORT"
)

mycursor = mydb.cursor(prepared=True)

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

def nuevaBoquilla(tamano):
    sql = "INSERT INTO Boquilla (Tamaño) VALUES (%s);"
    val=(tamano,)
    mycursor.execute(sql,val)
    mydb.commit()

reiniciaTabla("Boquilla")
nuevaBoquilla(17)
imprimeTabla("Boquilla")