#------------BD------------------
from tkinter import *
from tkinter import messagebox
import sqlite3

bdcursor=None
bdconexion=None

def conexionbd(): 
    global bdconexion, bdcursor
    bdconexion=sqlite3.connect("Usuarios")
    bdcursor=bdconexion.cursor()
    try:
        bdcursor.execute('''
                            CREATE TABLE DATOSUSUARIOS (
                                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                NOMBRE_U VARCHAR(50),
                                PASSWORD VARCHAR(15),
                                APELLIDO VARCHAR(50),
                                DIRECCION VARCHAR(50),
                                COMENTARIOS VARCHAR(100)
                            )
                        ''')
        messagebox.showinfo("BD", "Base de datos creada por exito" )
    except:
        messagebox.showwarning("Conectado","Conexion establecida")

def cerrarConexion():
    global bdconexion
    if bdconexion:
        bdconexion.close()
        bdconexion = None  # Resetea la variable para indicar que la conexión está cerrada
        messagebox.showinfo("Desconectado", "Conexión a la BD cerrada")
    else:
        messagebox.showwarning("Error cerrar","La conexion a la BD no esta abierta")
    

def salir(root):
    global bdconexion
    sal=messagebox.askquestion("Salir","Deseas salir?")
    if sal=="yes":
        if bdconexion:
            bdconexion.close()
        root.destroy()

#------------Ayuda-------------

def licencia():
    messagebox.showinfo("LICENCIA","Licencia tipo GNU")

def acercaDe():
    messagebox.showinfo("About","version:1.0\nutor: Idril_Diheroth\nlast update: 04/11/2024")
    
def nuevo(fr1, fr2):
    fr1.pack()
    fr2.pack(expand=1)

def cerrar(fr1, fr2):
    fr1.pack_forget()
    fr2.pack_forget()
    