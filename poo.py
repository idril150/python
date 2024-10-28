""" 
clase - modelo donde se redactan las caracteristicas comunes de un grupo
de objetos

Intancia - objeto perteneciente a una clase

modularización - permite reutilizar pedazos de codigo de un programa en otro

"""

""" class Coche():
    largoChasis=250
    anchoChasis=125         #4 prpiedades
    ruedas=4
    marcha=False
    
    def arrancar(self):
        self.marcha=True
        
    def estado(self):
        if(self.marcha):
            return "el coche a arrancado"       #2 comportamientos
        else:
            return "el coche era parado"

ferrari = Coche()

print(f"el coche mide {ferrari.largoChasis}cm de largo y {ferrari.anchoChasis}cm de ancho\nademas posee {ferrari.ruedas} ruedas")

print(ferrari.estado())
ferrari.arrancar()
print(ferrari.estado()) """


""" class Coche():
    
    def __init__(self):
        self.__largoChasis=250         #estado inicial
        self.__anchoChasis=125         #4 prpiedades
        self.__ruedas=4 #el __ antes del nombre de la variable la encapsula
        self.__marcha=False
    
    def arrancar(self, llave):
        if llave:
            self.__marcha=True
            if self.__chequeo():
                return "el coche esta en marcha"
            else:
                return "se detecto un problema en el coche no se a arrancado"
        else:
            self.__marcha=False
            return "el coche esta parado"
    
    def estado(self):
        print(f"el coche tiene {self.__ruedas} ruedas, un ancho de {self.__anchoChasis}cm\nun largo de {self.__largoChasis}cm")
    
    def __chequeo(self): #metodo encapsulado
        print("Realizando chequeo del carro")
        self.gasolina="ok"
        self.aceite="ok" 
        self.puertas="cerradas"
        if self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas":
            return True
        else:
            return False        
        

carro = Coche()
carro.estado()
print(carro.arrancar(True)) 

#segundo objeto
print("\n\nsegundo objeto")
carro2=Coche()
carro2.estado()
print(carro2.arrancar(False)) """


""" #HERENCIA
class Vehiculos():
    def __init__(self, marca, modelo):
        
        self.marca=marca
        self.modelo=modelo
        self.marcha=False
        self.acelera=False
        self.frena=False
    
    def arrancar(self):
        self.marcha=True
    
    def acelerar(self):
        self.acelera=True
    
    def frenar(self):
        self.frena=True
    
    def estado(self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nMarcha: {self.marcha}\nAcelera: {self.acelera}\nFrena: {self.frena}")
    
class Moto(Vehiculos):
    hcaballito=""
    
    def caballito(self):
        self.hcaballito="voy haciendo el caballito"

    def pararcaballito(self):
        self.hcaballito=""
    
    def estado(self):
        super().estado()
        print(f"{self.hcaballito}")
        
class Furgoneta(Vehiculos):
    
    def carga(self, cargar):
        self.cargado=cargar
        if(self.cargado==True):
            return "La furgneta esta cargada"
        else:
            return "la furgoneta no esta cargada"

class Velectrico(Vehiculos):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.cargando=False
        self.autonomia=100
    
    def cargaEnergia(self):
        self.cargando=True

class BicicletaElectrica(Velectrico, Vehiculos):
    pass

miMoto=Moto("honda", "CBR")
miMoto.estado()
miMoto.caballito()
miMoto.estado()
miMoto.pararcaballito()
miMoto.estado()

furgo=Furgoneta("Renault", "Kangoo")
furgo.arrancar()
furgo.estado()
print(furgo.carga(False))

bici=BicicletaElectrica("Orbea", "HC130")
bici.estado() """

""" #Herencia Super
class Persona():
    def __init__(self, name, age, direc):
      self.name = name
      self.age = age
      self.direc=direc
    
    def descripcion(self):
        print(f"nombre: {self.name} edad: {self.age} direccion: {self.direc}")

class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        self.salario=salario
        self.antiguedad=antiguedad
    
    def descripcion(self):
        super().descripcion()
        print(f"salario: {self.salario}, antiguedad: {self.antiguedad}")
        
victor=Empleado(1800,15,"Victor",24,"Chiapas")
victor.descripcion()

luis=Persona("Luis",27,"Mexico")


print(isinstance(victor, Persona))
print(isinstance(victor, Empleado))
print(isinstance(luis, Persona))
print(isinstance(luis, Empleado)) """

""" #polimorfismo

class Coche():
    
    def desplazamiento(self):
        print("Me desplazo utilizando 4 ruedas")

class Moto():
    
    def desplazamiento(self):
        print ("me desplazo utilizando 2 ruedas")

class Camion():
    
    def desplazamiento(self):
        print ("Me desplazo utilizando 6 ruedas")

def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()
    
camion=Camion()
coche=Coche()
moto=Moto()

desplazamientoVehiculo(camion)
desplazamientoVehiculo(coche)
desplazamientoVehiculo(moto) """

#metodos de cadenas
nombre="Victor Munoz rodas"
print(nombre.upper())
print(nombre.lower())
print(("tor" in nombre))
