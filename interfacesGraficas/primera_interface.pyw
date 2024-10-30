from tkinter import *

raiz=Tk()#genera la ventana raiz
raiz.title("primera ventan")
raiz.resizable(True,True)#determina si puede ser modificado su tamaño en ancho y alto

raiz.iconbitmap("gog.ico")#cambia el icono de la interfaz

#raiz.geometry("600x300") #configuracion del tamaño de la ventana de base la cual siempre se adaptara al tamaño del contenedor interno

raiz.config(background="red")#configuraciones de la ventana raiz

mainFrame=Frame()#creacion de un frame el cual debe empaquetarse
mainFrame.pack(side="bottom", expand=True)#configuracion de posicion y comportamiento en la ventana raiz
mainFrame.config(background="blue")
mainFrame.config(width="600",height="300")#configuracion del tamaño del frame con un tamaño fijo no adaptable
mainFrame.config(relief="groove", bd=35)
mainFrame.config(cursor="hand2")


raiz.mainloop()#para que la ventan pueda estar en ejecucion debe de estar en bucle infinto


