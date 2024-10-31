from tkinter import *

raiz = Tk()
miFrame = Frame(raiz, width=1200, height=600, bg="red")
miFrame.pack(side=TOP)

minombre=StringVar()
mapellido=StringVar()

cuadroNombre=Entry(miFrame, textvariable=minombre)
cuadroNombre.grid(row=0, column=1, padx=5)
cuadroNombre.config(fg="red", justify="center")

cuadroPassword=Entry(miFrame, textvariable=mapellido)
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

direccionLabel=Label(miFrame, text="Direccion")
direccionLabel.grid(row=3, column=0, sticky="e", padx=5, pady=10)

direccionLabel=Label(miFrame, text="Comentario")
direccionLabel.grid(row=4, column=0, sticky="e", padx=5, pady=10)

comentario=Text(miFrame, width=16, height=5)
comentario.grid(row=4,column=1, padx=5, pady=5)


scrolly=Scrollbar(miFrame, command=comentario.yview)
scrolly.grid(row=4,column=2, sticky="nsew", padx=0)
comentario.config(yscrollcommand=scrolly.set)

def codigoBoton():
    minombre.set("Victor")

def boton2():    
    mapellido.set(minombre.get())

boton=Button(raiz, text="Enviar", height=3, width=10, command=codigoBoton)
boton.pack()

boton2=Button(raiz, text="copiar", height=3, width=10, command=boton2)
boton2.pack()

raiz.mainloop()