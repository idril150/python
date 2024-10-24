""" def sum_n_nums(numbers):
    a=0
    print(type(numbers))
    for item in numbers:
        a+=item
    return a 

print(sum_n_nums([1,2,3,4,5,6,7,8,9,10]))
print(sum_n_nums([1,2,3,4,5])) """

""" lista=["hola","juan","pedro","pepe"]
lista.extend([32])
print(lista)
print(lista.index("pedro"))
print(lista[2]) """

""" tupla=("hola",32,"juan",True,"juan")
print(tupla)
print("juan" in tupla)
print(tupla.count("juan"))
print(len(tupla)) """

""" diccionari={"chiapas":"tuxtla","coahuila":"saltillo","mexico":"cdmx"}
print(diccionari["mexico"])
print(diccionari)
diccionari["tabasco"]="viyahermosa"
print(diccionari)
diccionari["tabasco"]="villa hermosa"
print(diccionari)
del diccionari["tabasco"]
print(diccionari) """

""" def sis (a):
    if a<5:
      print("a es menor que 5")
    elif(a==5):
        print("a es igual a 5")
    else:
        print("a es mayor que 5")
    
sis(5) """

""" for i in range(5, 51, 5):
    print(f"vuelta numero {i}")
 """
 
""" def hacer_si(a):
    while a<=10:
        print(a)
        a+=a        

hacer_si(1) """

""" def fibonacci_pyramid(levels):
    a, b = 0, 1
    index = 0
    for i in range(1, levels + 1):
        for j in range(i):
            print(a, end=" ")
            a, b = b, a + b
            index += 1
        print()
fibonacci_pyramid(6) """

""" a,b=0,1
for i in range(1,10,1):
    for j in range(i):
       print(a,b)
       a,b=b,a+b   
    print() """
    
# import mysql.connector

# config ={
#     'user':'root',
#     'password':'',
#     'host':'localhost',
#     'database':'db1'
# }

# cnx=mysql.connector.connect(**config)
# cursor = cnx.cursor()
# query = ("SELECT nombre FROM empleado")
# cursor.execute(query)
# for name in cursor:
#     print(name)
    
# def actualizar_empleado(id_empleado, nuevo_nombre, nuevo_bonop):
#     try:
#         # Conectar a la base de datos
#         cnx = mysql.connector.connect(**config)
#         cursor = cnx.cursor()

#         # Consulta para actualizar los valores del empleado
#         query = """
#         UPDATE empleado 
#         SET nombre = %s, bonop = %s 
#         WHERE id = %s
#         """
#         data = (nuevo_nombre, nuevo_bonop, id_empleado)

#         # Ejecutar la consulta
#         cursor.execute(query, data)

#         # Confirmar los cambios
#         cnx.commit()

#         print(f"Empleado con ID {id_empleado} ha sido actualizado.")

#     except mysql.connector.Error as err:
#         print(f"Error: {err}")
#     finally:
#         # Cerrar el cursor y la conexión
#         if cursor:
#             cursor.close()
#         if cnx:
#             cnx.close()

# actualizar_empleado(2, "Gustabo", 500.0)
# cnx.close

""" contador = 0
texto = "python tiene mucho poder matematico"
print(f"el texto '{texto}' tiene {len(texto)} caracteres")
for letra in texto:
    if letra==" ":
        continue
    contador+=1
    print(letra,end=" ")
print()
print(f"el texto '{texto}' tiene: {contador} letras") """


""" email=input("INTRODUCE TU EMAIL, POR FAVOR\n")
for i in email:
    if i == "@":
        arroba=True    
        break
else:#se ejecuta una vez se termina el ciclo for, al romper el ciclo esto se salta
    arroba=False

print(arroba) """

""" 
los generadores son estructuras que extraen valores de una funcion que se almacenan
en objetos iterables (que se pueden recorrer)

Se almacenan de uno en uno

cada vez que se almacena un valor, este permanecera en un estado pausado hasta que se solicita el siguiente
esta caracteristica es conocida como "suspension de estado" """

""" #funcion nomral
def gerarPares(limite):
    num=1
    lista=[]
    while num<limite:
        lista.append(num*2)
        num+=1
    return lista

print(gerarPares(10))

#generador
def gerarPares(limite):
    num=1
    while True:
        yield num*2
        num+=1

pares=gerarPares(10)

print(pares)
print(next(pares))
print("shfashdjfhsdjfhsaldkhfsd")
print(next(pares))
#entre llamada y llamada el objeto generador entra en un estado de suspención
 for i in pares:
    print(i) """ 

""" #Yield From
#cuando colocamos un asterisco antes de la entrada del argumento de una funcion indicamos que recibira un numero indeterminado de elementos
#ademas de que lo recibira en forma de tupla
def generaCiudades(*ciudades):
    for elemento in ciudades:
        #for sub in elemento: #el yield from nos evita usar este for
        yield from elemento

ciudades=generaCiudades("Tuxtla","tapachula","San cristobal", "Arriaga")
print(next(ciudades))
print(next(ciudades)) """

#excepciones
#una excepcion es un error en tiempo de ejecucion, cuando hay un programa correctamente escrito
#pero durante la ejecucion del programa ocurre un error inesperado no previsto
""" def sum(num1,num2):
    return num1+num2

def res(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    
    try:
        return num1/num2
    except ZeroDivisionError:
        print("no se puede dividir entre 0")
        return "operacion erronea"


while True:
    try:
        op1=(int(input("introduce el primer numero: ")))
        op2=(int(input("introduce el segundo numero: ")))
        break
    except ValueError:
        print("ERROR SOLO SE ACEPTAN NUMEROS NUMEROS ENTEROS, INTENTA DE NUEVO")



while True:
    operacion=(input("introduce la operacion a realisar (sum,res,mul,div): "))
    if operacion=="sum":
        print(sum(op1,op2))
        break

    elif operacion=="res": 
        print(res(op1,op2))
        break

    elif operacion=="mul":   
        print(mul(op1,op2))
        break

    elif operacion=="div":  
        print(div(op1,op2))
        break
    
    else:
        print("opcion erronea")

print("operacion ejecutasda, continuacion de ejecucion del programa") """

""" def divide():
    while True:
        try:
            op1=(float(input("introduce un numero: ")))
            op2=(float(input("introduce otro numero: ")))            
            print(f"la division es: {op1/op2}")
            break
        except ValueError:
            print("el valor introducido es erroneo")
        except ZeroDivisionError:
            # captura de errores consecutivos
            print("no puede dividirse entre cero")
        finally:#finally se ejecuta si o si
            print("fin del calculo")
    
def divide1():
    while True:
        try:
            op1=(float(input("introduce un numero: ")))
            op2=(float(input("introduce otro numero: ")))            
            print(f"la division es: {op1/op2}")
            break
        except:
            print("error")
    print("fin del calculo")

divide() """

""" #Lanzamiento de excepciones de forma intencionada
def evaluaEdad(edad):
    
    if edad<=0:
        raise ValueError("No se permiten edades negativas")
    
    if edad<20:
        return "eres muy joven"
    elif edad<40:
        return "eres joven"
    elif edad<65:
        return "ya no eres joven"
    elif edad>64:
        return "cuidate"

print(evaluaEdad(-18)) """

import math

def raiz(num):
    if num<0:
        raise TypeError("el numero no puede ser negativo")
    else:
        return math.sqrt(num)
    
while True:
    try:
        print(raiz(int(input("introduce un numero "))))
        break
    except ValueError:
        print("debe introducir un valor numerico")
    except TypeError as ErrordeRango:
        print(ErrordeRango)
print("programa continuando")