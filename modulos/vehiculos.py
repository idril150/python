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
        if self.frena:
            self.frena=False
        self.acelera=True
        
    
    def frenar(self):
        if self.acelera:
            self.acelera=False
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