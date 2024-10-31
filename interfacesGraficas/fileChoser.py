from tkinter import *
from tkinter import filedialog

root=Tk()


def abrirFichero():                                     #Ruta de inicio         #tipos de ficheros
    fichero=filedialog.askopenfilename(title="Abrir",initialdir="C:/", filetypes=(("Ficheros de excel","*.xlsx" ),
                                                                                 ("Ficheros de texto","*.txt"),
                                                                                 ("todos los ficheros","*.*")))#nos devuelve la ruta del fichero
    print(fichero)

Button(root, text="abrir", command=abrirFichero).pack()


root.mainloop()