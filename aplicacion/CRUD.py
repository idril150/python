from tkinter import *
import CRUDFunc as crfun
import menusfunc as mfun
#-------------funciones----------------


root=Tk()
bmenu=Menu(root)
root.config(menu=bmenu, width=300, height=300)
crfun.iniciarvariables()


bdmenu=Menu(bmenu, tearoff=0)
bdmenu.add_command(label="Conectar", command=mfun.conexionbd)
bdmenu.add_command(label="Desconectar", command=mfun.cerrarConexion)
bdmenu.add_separator()
bdmenu.add_command(label="Salir", command=lambda:mfun.salir(root))


borramenu=Menu(bmenu, tearoff=0)
borramenu.add_command(label="Borrar cambios", command=crfun.limpiarCampos)

crudMenu=Menu(bmenu, tearoff=0)

crudMenu.add_command(label="Crear", command=crfun.crear)
crudMenu.add_command(label="Buscar", command=crfun.encontrar)
crudMenu.add_command(label="Actualizar", command=crfun.actualizar)
crudMenu.add_command(label="Borrar", command=crfun.eliminar)

ayudaMenu=Menu(bmenu, tearoff=0)
ayudaMenu.add_command(label="Licencia", command=mfun.licencia)
ayudaMenu.add_command(label="Acerca de", command=mfun.acercaDe)




#----comienzo de campos------
frame1=Frame(root)


Label(frame1, text="id").grid(row=0, column=0, padx=10, pady=10, sticky="e")
eID=Entry(frame1, textvariable=crfun.varId)
eID.grid(row=0, column=1, padx=10, pady=10)

Label(frame1, text="Nombre").grid(row=1, column=0, padx=10, pady=10, sticky="e")
eNom=Entry(frame1, textvariable=crfun.varNom)
eNom.grid(row=1, column=1, padx=10, pady=10)
eNom.config(justify="right", fg="red")

Label(frame1, text="Contraseña").grid(row=2, column=0, padx=10, pady=10, sticky="e")
ePass=Entry(frame1, textvariable=crfun.varPass)
ePass.grid(row=2, column=1, padx=10, pady=10)
ePass.config(show="*")

Label(frame1, text="Apellido").grid(row=3, column=0, padx=10, pady=10, sticky="e")
eApe=Entry(frame1, textvariable=crfun.varApe)
eApe.grid(row=3, column=1, padx=10, pady=10)
eApe.config(justify="right", fg="red")

Label(frame1, text="Direccion").grid(row=4, column=0, padx=10, pady=10, sticky="e")
eDir=Entry(frame1, textvariable=crfun.varDir)
eDir.grid(row=4, column=1, padx=10, pady=10)
eDir.config(justify="right", fg="red")

Label(frame1, text="Comentario").grid(row=5, column=0, padx=10, pady=10, sticky="e")
crfun.tComen=Text(frame1, width=16, height=8)
crfun.tComen.grid(row=5, column=1, padx=10, pady=10)
scrollV=Scrollbar(frame1, command=crfun.tComen.yview)
scrollV.grid(row=5, column=2, sticky="nsew", padx=10, pady=10)

crfun.tComen.config(yscrollcommand=scrollV.set)

#--------Frame inferior-----------
frame2=Frame(root)


Button(frame2, text="Agregar", command=crfun.crear).grid(row=0, column=0, padx=10, pady=10)
Button(frame2, text="Buscar", command=crfun.encontrar).grid(row=0, column=1, padx=10, pady=10)
Button(frame2, text="Editar", command=crfun.actualizar).grid(row=0, column=2, padx=10, pady=10)
Button(frame2, text="Eliminar", command=crfun.eliminar).grid(row=0, column=3, padx=10, pady=10)

archivo=Menu(bmenu, tearoff=0)
archivo.add_command(label="Nuevo", command=lambda:mfun.nuevo(frame1, frame2))
archivo.add_command(label="cerrar", command=lambda:mfun.cerrar(frame1,frame2))
bmenu.add_cascade(label="Archivo",menu=archivo)
bmenu.add_cascade(label="BD", menu=bdmenu)
bmenu.add_cascade(label="Borrar", menu=borramenu)
bmenu.add_cascade(label="CRUD", menu=crudMenu)
bmenu.add_cascade(label="Ayuda", menu=ayudaMenu)
root.mainloop()