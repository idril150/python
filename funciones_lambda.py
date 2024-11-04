#la funcion lambda nos sirve para que las funciones sencillas se resuman mucho mas
""" #Funcion normal sencilla
def areaTriangulo(a,b):
    return (a*b)/2

print(areaTriangulo(1,5)) """

#Funcion Lambdad
areaRectangulo=lambda a,b:a*b
areaTriangulo=lambda a,b:areaRectangulo(a,b)/2
print(areaTriangulo(3,5))
print(areaTriangulo(5,5))
print(areaRectangulo(2,3))

#funcion lambda con if sencillo
pesos=lambda val: f"¡{val+.00}$!" if type(val) == int else f"¡{val+.00}$!"
comision_dinero=15585.35
print(pesos(comision_dinero))