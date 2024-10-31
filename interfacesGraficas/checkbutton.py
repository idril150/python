from tkinter import *

root=Tk()
root.title("checkButton")

playa=IntVar()
sol=IntVar()
sexo=IntVar()
foto=PhotoImage(file="pajaro.png")
poto=Label(root, image=foto, width=100, height=100)

def pideCuuerpo():
    opcionEscogida=""
    if(playa.get() == 1):
        opcionEscogida+=" playa,"
    if(sol.get() == 1):
        opcionEscogida+=" sol,"
    if(sexo.get() == 1):
        poto.config()
        if playa.get() == 1 or sol.get() == 1:
            opcionEscogida+=" y sexo"
        else:
            opcionEscogida +=" sexo"
    textofin.config(text=f"mi cuerpo pide{opcionEscogida}")


poto.grid(row=0, column=0, sticky="n")
famre=Frame(root)
famre.grid(row=1, column=0)
Checkbutton(famre, text="Playa", variable=playa, onvalue=1, offvalue=0, command=pideCuuerpo).grid(row=0, column=0, sticky="w", padx=5, pady=5)
Checkbutton(famre, text="sol", variable=sol, onvalue=1, offvalue=0, command=pideCuuerpo).grid(row=1, column=0, sticky="w", padx=5, pady=5)
Checkbutton(famre, text="sexo", variable=sexo, onvalue=1, offvalue=0, command=pideCuuerpo).grid(row=2, column=0, sticky="w", padx=5, pady=5)

textofin=Label(famre)
textofin.grid(row=3,column=0)


root.mainloop()