""" 
Entry son entradas de texto
"""

from tkinter import *

raiz = Tk()
miFrame = Frame(raiz, width=1200, height=600, bg="red")
miFrame.pack(side=TOP)

cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=0, column=1, padx=5)
cuadroNombre.config(fg="red", justify="center")

cuadroPassword=Entry(miFrame)
cuadroPassword.grid(row=1, column=1, padx=5)
cuadroPassword.config(fg="red", justify="right", show="*")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2, column=1, padx=5)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, padx=5)

nombreLabel=Label(miFrame, text="Nombre")
nombreLabel.grid(row=0, column=0, sticky="E", padx=5, pady=10)

passwordLabel=Label(miFrame, text="Password")
passwordLabel.grid(row=1, column=0, sticky="E", padx=5, pady=10)

apellidoLabel=Label(miFrame, text="Apellido")
apellidoLabel.grid(row=2, column=0, sticky="E", padx=5, pady=10)

direccionLabel=Label(miFrame, text="Direccion de casa")
direccionLabel.grid(row=3, column=0, sticky="e", padx=5, pady=10)



raiz.mainloop()