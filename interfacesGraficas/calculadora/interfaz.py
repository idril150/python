from tkinter import *
import opera

root=Tk()
frame=Frame(root, bg="#8845c9", width=100, height=100)
frame.pack(side=TOP)

buss=[]
op=[]
disP=StringVar()
global calcu
def sig(s):#metodo para seleccionar operacion a realizar
    buss.append(float(disP.get()))
    op.append(s)
    print(op)
    disP.set("")

def dell():
    buss.clear()
    op.clear()
    disP.set("")    

def inser(a):#metodo para incertar numeros
    disP.set(disP.get()+a)

def resul():#metodo para calcular el resultado
    buss.append(float(disP.get()))
    cal=opera.calculo(buss,op)#llaada a la clase opera donde se realizan los calculos
    print(cal)
    disP.set(cal)

label1=Label(frame, textvariable=disP, bg="#FFFFFF", height=2, width=15, font=20)
label1.grid(row=0, columnspan=5, padx=2, pady=5)

boton1=Button(frame, text="1", command=lambda:inser("1"), height=2, width=3).grid(row=1, column=0, padx=2, pady=5)
boton2=Button(frame, text="2", command=lambda:inser("2"), height=2, width=3).grid(row=1, column=1, padx=2, pady=5)
boton3=Button(frame, text="3", command=lambda:inser("3"), height=2, width=3).grid(row=1, column=2, padx=2, pady=5)
botonMul=Button(frame, text="*", command=lambda:sig("*"), height=2, width=3).grid(row=1, column=3, padx=2, pady=5)
botonDel=Button(frame, text="<-", command=dell, height=2, width=3).grid(row=1, column=4, padx=2, pady=5)
boton4=Button(frame, text="4", command=lambda:inser("4"), height=2, width=3).grid(row=2, column=0, padx=2, pady=5)
boton5=Button(frame, text="5", command=lambda:inser("5"), height=2, width=3).grid(row=2, column=1, padx=2, pady=5)
boton6=Button(frame, text="6", command=lambda:inser("6"), height=2, width=3).grid(row=2, column=2, padx=2, pady=5)
botonDiv=Button(frame, text="/", command=lambda:sig("/"), height=2, width=3).grid(row=2, column=3, padx=2, pady=5)
botonRes=Button(frame, text="-", command=lambda:sig("-"), height=2, width=3).grid(row=2, column=4, padx=2, pady=5)
boton7=Button(frame, text="7", command=lambda:inser("7"), height=2, width=3).grid(row=3, column=0, padx=2, pady=5)
boton8=Button(frame, text="8", command=lambda:inser("8"), height=2, width=3).grid(row=3, column=1, padx=2, pady=5)
boton9=Button(frame, text="9", command=lambda:inser("9"), height=2, width=3).grid(row=3, column=2, padx=2, pady=5)
botonSum=Button(frame, text="+", command=lambda:sig("+"), height=2, width=3).grid(row=3, column=3, padx=2, pady=5)
botonIg=Button(frame, text="=", command=resul, height=6, width=3).grid(row=3, column=4, padx=2, pady=5, rowspan=2)
boton0=Button(frame, text="0", command=lambda:inser("0"), height=2, width=8).grid(row=4, column=0, padx=2, pady=5, columnspan=2)
botonP=Button(frame, text=".", command=lambda:inser("."), height=2, width=3,).grid(row=4, column=2, padx=2, pady=5)
botonSum=Button(frame, text="^", command=lambda:sig("**"), height=2, width=3).grid(row=4, column=3, padx=2, pady=5)

root.mainloop()