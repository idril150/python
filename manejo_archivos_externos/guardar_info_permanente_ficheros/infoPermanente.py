import pickle
#guardado de datos permanentes en ficheros
class persona ():
    def __init__ (self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print(f"se ha creado un objeto con el nombre: {self.nombre}")
    
    def __str__ (self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)
    
    def descripcion(self):
        print(f"nombre: {self.nombre}\ngenero: {self.genero}\nedad: {self.edad}")

class ListaPersonas:
    
    personas=[]
    
    def __init__ (self):
        listadePersonas=open("personas", "ab+")
        listadePersonas.seek(0)
        
        try:
            self.personas=pickle.load(listadePersonas)
            print("se cargaron {} personas del fichero externo".format(len(self.personas)))
        except:
            print("el fichero esta vacio")
        finally:
            listadePersonas.close()
            del(listadePersonas)
    
    def agregarPersonas(self, persona):
        self.personas.append(persona)
        self.guardarPersonaEnFichero()
    
    def mostrarInfo(self):
        for persona in self.personas:
            print(persona)
    
    def guardarPersonaEnFichero(self):
        listadePersonas=open("personas","wb")
        pickle.dump(self.personas,listadePersonas)
        listadePersonas.close()
        del(listadePersonas)
        
    def mostrarInfoFichero(self):
        print("la informaion el fichero externo es la siguiente:")
        for persona in self.personas:
            print(persona)

listaP=ListaPersonas()
      
p1=persona("Victor","Masculino",24)
listaP.agregarPersonas(p1)
listaP.mostrarInfoFichero()
print(12*5)