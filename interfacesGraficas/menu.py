from tkinter import *

root=Tk()

bmenu=Menu(root)
root.config(menu=bmenu, width=300, height=300)#se agrega el menu a la configuracion del root

archivoMenu=Menu(bmenu, tearoff=0)#se crean los elementos del elementos en el menu
#-----agregar opciones al sub menu-------
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_separator()
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar")
archivoMenu.add_command(label="Salir")


edicionMenu=Menu(bmenu, tearoff=0)#y se le hae perteneciente a la barra de menu
#-----agregar opciones al sub menu-------
edicionMenu.add_command(label="Copiar")
edicionMenu.add_command(label="Cortar")
edicionMenu.add_separator()
edicionMenu.add_command(label="Pegar")

herramientasMenu=Menu(bmenu, tearoff=0)
#-----agregar opciones al sub menu-------



ayudaMenu=Menu(bmenu, tearoff=0)
#-----agregar opciones al sub menu-------
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="About")


#----agrega el texto a mostrar y se le relaciona con un elemento del menu-----
bmenu.add_cascade(label="Archivo", menu=archivoMenu)
bmenu.add_cascade(label="Edicion", menu=edicionMenu)
bmenu.add_cascade(label="Herramientas", menu=herramientasMenu)
bmenu.add_cascade(label="Ayuda", menu=ayudaMenu)




root.mainloop()