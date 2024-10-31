import sqlite3

#----se cra la conexion y con ella la base de datos si aun no existe----

bdconexion=sqlite3.connect("primerabase")

#----creacion del cursor-------
bdCursor=bdconexion.cursor()

#-----ejecutar consulta-------
#----creacion de tabla productos----
#bdCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")
#-----ingresar datos a tabla productos----
bdCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON',30,'DEPORTES')")
bdconexion.commit()


#--------------Cerrar la conexion------------
bdconexion.close()