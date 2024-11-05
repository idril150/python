""" numeros=[5,4,3,6,7,8,1,0,2]
print(list(filter(lambda num: num%2==0 and not num==0, numeros)))

numerospares=list(filter(lambda num: not num%2 and not num==0 , numeros))

numerospares.sort()
print(numerospares) """

class Empleado:
    def __init__(self, nombre, zona, salario):
        self.nombre = nombre
        self.zona = zona
        self.salario = salario
    
    def __str__(self):
        return "{} trabaja en: {} y tiene un salario de: {}$".format(self.nombre, self.zona, self.salario)
    
listaempleados=[
    Empleado("VICTOR","OFICINA",4250),
    Empleado("JAVI","YUMKA",6050),
    Empleado("GRIS","OFICINA",5400),
    Empleado("LUIS","OFICINA",4000),
    Empleado("MAR","YUMKA",3600),
    Empleado("JUAN","ZOOMAT",4250)
]

def mostrar(li):
    for i in li:
        print(i)

oficina=filter(lambda empleado: empleado.zona=="OFICINA", listaempleados)
yumka=filter(lambda empleado: empleado.zona=="YUMKA", listaempleados)
zoomat=filter(lambda empleado: empleado.zona=="ZOOMAT", listaempleados)

mostrar(oficina)
mostrar(yumka)
mostrar(zoomat)

