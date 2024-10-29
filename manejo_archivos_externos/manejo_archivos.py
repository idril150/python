#from io import open
#para el manejo de archivos externos se utiliza la biblioteca io
""" #modo escritura con w de write
archivo_texto=open("configs.txt", "w")
oracion="hola amigos\ncomo estan?"
archivo_texto.write(oracion)
archivo_texto.close() """

""" #modo lectura
archivo_texto=open("configs.txt", "r")
#ingresar todo el texto en una variable con r de read
texto=archivo_texto.read()
archivo_texto.close()
print(texto) """
""" #ingresar el texto en listas
textos=archivo_texto.readlines()
archivo_texto.close()
print(textos)
for texto in textos:
    print(texto) """

""" #escritura de nueva linea con a de append
archivo_texto=open("configs.txt", "a")
archivo_texto.write("\nnueva linea")
archivo_texto.close() """

""" archivo_texto=open("configs.txt", "r")

print(archivo_texto.read(11),"/n")

archivo_texto.seek(21)#situa el puntero en el archivo de texto en la posicion del caracter especificado
print(archivo_texto.read(2))#a partir de la posicion del puntero podemos determinar cuantos caracteres leer

archivo_texto.seek(len(archivo_texto.read())/2)#la funcion len nos devuelve la longitud del texto, y luego al dividirlo entre 2 nos devuelve la mitad del texto
print(archivo_texto.read()) """

""" #modo lectura y escritura con r+ 
archivo_texto=open("configs.txt", "r+")
#print(archivo_texto.readlines())
lista_texto=archivo_texto.readlines()
lista_texto[1]="esta es la linea 2 ahora, se incluyo desde python\n"
archivo_texto.seek(0)
archivo_texto.writelines(lista_texto)
archivo_texto.close() """

