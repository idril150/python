import sqlite3

bdconexion=sqlite3.connect("gestionProductos")
bdcursor=bdconexion.cursor()

bdcursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='ELECTRONICA'")
a=bdcursor.fetchall()
print(a)

bdcursor.execute("UPDATE PRODUCTOS SET PRECIO=25 WHERE ID=6")   #ACTUALIZACION DE DATOS

bdcursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='ELECTRONICA'")
a=bdcursor.fetchall()
print(a)

bdconexion.commit()
bdconexion.close()