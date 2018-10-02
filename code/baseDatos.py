import mysql.connector
mydb=  mysql.connector.connect(
    host="HOST",
    user="USER",
    passwd="PASSWORD",
    db="colaImpresionTfg",
    port="PORT"
)

mycursor = mydb.cursor(prepared=True)

def imprimeColumnas(nombre):
    val=nombre
    mycursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '%s'",val)
    for x in mycursor:
        print(x)

def imprimeTabla(nombre):
    sql="SELECT * FROM %s"
    val=(nombre,)
    mycursor.execute(sql,val)
    for x in mycursor.fetchall():
        print(x)


def nuevaBoquilla(tamano):
    sql = "INSERT INTO Boquilla (Tamaño) VALUES ("+tamano+")"
    mycursor.execute(sql,tamano)
    mydb.commit()

# imprimeColumnas("Pedido")
# nuevaBoquilla("0.5")
imprimeTabla("Boquilla")
