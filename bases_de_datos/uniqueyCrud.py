import sqlite3

bdconexion=sqlite3.connect("gestionProductos")
bdcursor=bdconexion.cursor()

#bdcursor.execute("INSERT INTO PRODUCTOS VALUES (NULL, 'AUDIFONOS', 20, 'ELECTRONICA')")#CREATE

bdcursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='ELECTRONICA'") #READ
a=bdcursor.fetchall()
print(a)

bdcursor.execute("UPDATE PRODUCTOS SET PRECIO=25 WHERE ID=7")   #UPDATE DE DATOS

bdcursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='ELECTRONICA'")
a=bdcursor.fetchall()
print(a)

bdcursor.execute("DELETE FROM PRODUCTOS WHERE ID=08")#DELETE
bdcursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='ELECTRONICA'")
a=bdcursor.fetchall()
print(a)

bdconexion.commit()
bdconexion.close()