import mysql.connector

# Configuración de la conexión
config ={
    'user':'root',
    'password':'',
    'host':'localhost',
    'database':'db1'
}

# Conectar a la base de datos
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

getEmpleadosBd1 = ("SELECT id, bonop, estado, nombre, salario, destino_id, clasificacion_id1, clasificasion_id2 FROM empleado")
cursor.execute(getEmpleadosBd1)

# Recorrer e imprimir los resultados
for (id, bonop, estado, nombre, salario, destino_id, clasificacion_id1, clasificasion_id2) in cursor:
    
    print(f"ID: {id}, Bono: {bonop}, Estado: {estado}, Nombre: {nombre}, Salario: {salario}, "f"Destino ID: {destino_id}, Clasificación ID 1: {clasificacion_id1}, Clasificación ID 2: {clasificasion_id2}")

# Cerrar cursor y conexión
cursor.close()
cnx.close()
