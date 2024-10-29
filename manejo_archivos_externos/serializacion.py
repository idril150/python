import pickle
""" #Serializacion de colecciones Bibliotecas necesarias: Pickle
lista_nombres=["pedro","pablo","Victor","Georgina"]
fichero_binario=open("lista_nombres","wb")
#volcamos la lista en el fichero que crearemos usando pickle.dump
pickle.dump(lista_nombres, fichero_binario)
fichero_binario.close()
del (fichero_binario) """
""" #se crea el fichero cifrado en binario, ahora se rescata la informacion
fichero=open("lista_nombres", "rb")
lista=pickle.load(fichero)
print(lista) """

""" #serializacion de objetos, sigue usando se la biblioteca pickle
class vehiculos():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.acelera = False
        self.frena = False
        self.enmarcha = False
    
    def acelerar(self):
        if not self.enmarcha:
            return
        if self.frena:
            self.frena = False
        self.acelera = True
    
    def frenar(self):
        if self.acelera:
            self.acelera = False
        self.frena=True
    
    def marcha(self):
        self.enmarcha=True
    
    def estado(self):
        print(f"marca: {self.marca}\nmodelo: {self.modelo}\n    acelerador: {self.acelera}\n    freno: {self.frena}\n    enmarcha: {self.enmarcha} ") """

""" #volcado de objetos en binario
coche1=vehiculos("honda","124")
coche2=vehiculos("mazda","1998")
coche3=vehiculos("hbc","max4")

coches=[coche1,coche2,coche3]

fichero=open("coches", "wb")
pickle.dump(coches, fichero)
fichero.close()
del(fichero) """

""" #recuperacion de objetos serializados
ficheroA=open("coches", "rb")
coches=pickle.load(ficheroA)
ficheroA.close()

for coche in coches:
    print(coche.estado()) """

