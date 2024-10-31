from tkinter import *

root=Tk()
varOpcion=IntVar()
def impri():
    if varOpcion.get()==1:
        etiqueta.config(text="eres macho")
    elif varOpcion.get()==2:
        etiqueta.config(text="eres macha")
    else:
        etiqueta.config(text="eres un helicoptero apache de combate")

#deben tener una variable compartida a la cual dar un alor numerico al pulsarlo
#se les puede asignar  una funcion para darle funcionalidad
Label(root,text="genero:").grid(row=0, column=1)
Radiobutton(root, text="masculino", variable=varOpcion, value=1, command=impri ).grid(row=1, column=0)
Radiobutton(root, text="femenino", variable=varOpcion, value=2, command=impri ).grid(row=1, column=1)
Radiobutton(root, text="otro", variable=varOpcion, value=3, command=impri ).grid(row=1, column=2)

etiqueta=Label(root)
etiqueta.grid(row=2, column=0, columnspan=3)

root.mainloop()