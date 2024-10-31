import sqlite3

bdconexion=sqlite3.connect("gestionProductos")
bdcursor=bdconexion.cursor()

bdcursor.execute("""--sql
                CREATE TABLE PRODUCTOS (
                     ID INTEGER PRIMARY KEY AUTOINCREMENT,
                     NOMBRE_ARTICULO VARCHAR(50),
                     PRECIO INTEGER,
                     SECCION VARCHAR(20)
                )
                """)

productos=  [
                ("PELOTA", 1, "JUGUETERIA"),
                ("PANTALON", 1, "ROPA"),
                ("DESARMADOR", 3, "FERRETERIA"),
                ("JARRON", 10, "CERAMICA"),
                ("PC", 1500, "ELECTRONICA"),
            ]

bdcursor.executemany("INSERT INTO PRODUCTOS VALUES (null,?,?,?)", productos)

bdconexion.commit()
bdconexion.close()