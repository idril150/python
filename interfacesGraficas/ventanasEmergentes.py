from tkinter import *
from tkinter import messagebox #libreria necesaria para los mensajes emergentes

root=Tk()

def infoAdicional():
    messagebox.showinfo("ventanas","Ventanas version 1.0")

def infoLicencia():
    messagebox.showwarning("Licencia","Producto bajo licencia GNU")

def salir():
    # a=messagebox.askquestion("Salir","Deseas salir?")
    a=messagebox.askokcancel("Salir","Deseas salir?")
    if a==True:
        root.destroy()

def cerrarDoc():
    a=messagebox.askretrycancel("Reintentar","no fue posible guardar el documento\n¿desea volver a intetntarlo?")
    if a == False:
        root.destroy()
        
bmenu=Menu(root)
root.config(menu=bmenu, width=300, height=300)

archivoMenu=Menu(bmenu, tearoff=0)

archivoMenu.add_command(label="Nuevo")
archivoMenu.add_separator()
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=cerrarDoc)
archivoMenu.add_command(label="Salir", command=salir)


edicionMenu=Menu(bmenu, tearoff=0)
edicionMenu.add_command(label="Copiar")
edicionMenu.add_command(label="Cortar")
edicionMenu.add_separator()
edicionMenu.add_command(label="Pegar")

herramientasMenu=Menu(bmenu, tearoff=0)


ayudaMenu=Menu(bmenu, tearoff=0)

ayudaMenu.add_command(label="Licencia", command=infoLicencia)
ayudaMenu.add_command(label="About", command=infoAdicional)

bmenu.add_cascade(label="Archivo", menu=archivoMenu)
bmenu.add_cascade(label="Edicion", menu=edicionMenu)
bmenu.add_cascade(label="Herramientas", menu=herramientasMenu)
bmenu.add_cascade(label="Ayuda", menu=ayudaMenu)


root.mainloop()