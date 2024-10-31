from tkinter import *
root=Tk()
def ventana():
    root.destroy()
    root2=Tk()
    root2.config(bg="#8420f0")
    
    def cerrar():
        root2.destroy()
    Button(root2, text="cerrar", command=cerrar).pack()
    root2.mainloop()
Button(root, text="abrir", command=ventana).pack()
root.mainloop()