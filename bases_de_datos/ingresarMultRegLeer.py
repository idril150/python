import sqlite3

#----se cra la conexion y con ella la base de datos si aun no existe----

bdconexion=sqlite3.connect("primerabase")

#----creacion del cursor-------
bdCursor=bdconexion.cursor()


""" #---CREACION DE TUPLA PARA MULTIPLE CARGA DE REGISTROS
variosProductos=[
    ("CAMISETA", 10, "DEPORTES",),
    ("JARRON", 90, "CERAMICA",),
    ("CAMION", 15, "JUGUETES",)
]

bdCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos) """

#----OBTENCION DE REGISTROS----
bdCursor.execute("SELECT * FROM PRODUCTOS")
variosProductos=bdCursor.fetchall()
#print(variosProductos)
for producto in variosProductos:
    print(f"producto: {producto[0]}, precio: {producto[1]}, seccion: {producto[2]}")
bdconexion.commit()



bdconexion.close()