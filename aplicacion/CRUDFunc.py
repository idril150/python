from tkinter import *
from tkinter import messagebox
import menusfunc as mfun

varId=None
varNom=None
varApe=None
varPass=None
varDir=None
tComen=None


def iniciarvariables():
    global varId, varNom, varApe, varPass, varDir, tComen
    varId=StringVar()
    varNom=StringVar()
    varApe=StringVar()
    varPass=StringVar()
    varDir=StringVar()

def limpiarCampos():
    global varDir, varNom, varApe, varPass, varId, tComen
    varId.set("")
    varApe.set("")
    varDir.set("")
    varNom.set("")
    varPass.set("")
    if tComen is not None:
        tComen.delete(1.0,END)

def crear():
    global varDir, varNom, varApe, varPass, varId, tComen
    if mfun.bdconexion:
        try:        
            datos=varNom.get(),varPass.get(),varApe.get(),varDir.get(),tComen.get(1.0,END)
            mfun.bdcursor.execute("INSERT INTO DATOSUSUARIOS VALUES (NULL, ?,?,?,?,?)",(datos))
            mfun.bdconexion.commit()
            messagebox.showinfo("Sucess", f"se guardo el usuario {varNom.get()}")
        except:
            messagebox.showerror("Error"," al guardar el usuario")
    else:
        messagebox.showerror("Error","Base de datos desconectada")

def encontrar():
    global varDir, varNom, varApe, varPass, varId, tComen
    if mfun.bdconexion:
        mfun.bdcursor.execute(f"SELECT * FROM DATOSUSUARIOS WHERE ID='{int(varId.get())}'")
        datos=mfun.bdcursor.fetchone()
        mfun.bdconexion.commit()
        if datos:
            varId.set(datos[0])
            varNom.set(datos[1])
            varPass.set(datos[2])
            varApe.set(datos[3])
            varDir.set(datos[4])
            tComen.delete(1.0,END)
            tComen.insert(1.0,datos[5])
            return datos[2]
        else: 
            messagebox.showerror("Error","Usuario no encontrado")
    else:
        messagebox.showerror("Error","Base de datos desconectada")

def eliminar():
    global varDir, varNom, varApe, varPass, varId, tComen
    if mfun.bdconexion:
        a=messagebox.askokcancel("warning",f"desea eliminar al usuario usuario con id: {varId.get()}?")
        if a:
            mfun.bdcursor.execute(f"DELETE FROM DATOSUSUARIOS WHERE ID='{int(varId.get())}'")
            mfun.bdconexion.commit()        
    else:
        messagebox.showerror("Error","Base de datos desconectada")    
    limpiarCampos() 
    

def actualizar():
    global varDir, varNom, varApe, varPass, varId, tComen
    if mfun.bdconexion:
        a=messagebox.askokcancel("WARNING", f"desea eliminar al usuario: {varNom.get()}?")
        if a:
            datos=varNom.get(),varPass.get(),varApe.get(),varDir.get(),tComen.get(1.0,END)
            mfun.bdcursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_U=?, PASSWORD=?, APELLIDO=?, DIRECCION=?, COMENTARIOS=?",(datos))
            #mfun.bdcursor.execute(f"UPDATE DATOSUSUARIOS SET NOMBRE_U='{varNom.get()}', PASSWORD='{varPass.get()}', APELLIDO='{varApe.get()}', DIRECCION='{varDir.get()}', COMENTARIOS='{tComen.get(1.0,END)}'  WHERE ID='{(int(varId.get()))}'")
            mfun.bdconexion.commit()
    else:
        messagebox.showerror("Error","Base de datos desconectada")
        
    