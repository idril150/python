from tkinter import *

root=Tk()
miFrame=Frame(root, width=500, height=400, bg="#800000")
miFrame.pack(side=TOP, fill="both", expand=1)
miImagen=PhotoImage(file="LOGOS VARIACION DE COLORES.png")
#miLabel= Label(miFrame, text="Hola mundo", bg="#FFFFFF", fg="#2045F8", font=("Comic Sans MS",18)).place(x=10, y=10)#cantidad de pixeles en espacio tomando como 0,0 la esquina superior isquierda
Label(miFrame, image=miImagen).place(x=10,y=10)
root.mainloop()
#la libreria tkinter permite png y gif