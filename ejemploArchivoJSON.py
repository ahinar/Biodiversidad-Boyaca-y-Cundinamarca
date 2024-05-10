#Ejemplo de archivo texto
##archivo = open('datos4.txt','r') #Se abre datos4.txt, tipo lectura (r)
###Se leen los datos del archivo
##for linea in archivo:
##  print(linea)
#archivo.close() #Se cierra el archivo (no debe faltar)
#Ejemplo de escritura de archivo
##archivo2 = open('datos5.txt','w') #Se abre datos5.txt, tipo escritura
##archivo2.write("Falta poco\n") #Se escribe una línea, con retorno a nueva línea
##archivo2.write("Lo importante es aprender\n")
##archivo2.write("Y terminar las tareas\n")
##archivo2.close()
#Abrir un archivo para agregar líneas
##archivo3 = open('datos5.txt','a')
###Se abre el archivo para agregar a continuación
##archivo3.write("Ante todo, dedicar esfuerzo\n")
##archivo3.write("manteniendo la capacidad de aprender\n")
##archivo3.write("este lenguaje es poderoso\n")
##archivo3.close()
#Leer archivo JSON y armar diccionarios y meterlos en una lista
import json
mi_lista=[]  #Se crea una lista vacía
try:
    archivo = open('ejemplodic3.json','r') 
    linea = archivo.readline()  #Lee una línea del archivo
    while linea !="":  #mientras el archivo tenga líneas
        #Convertir la línea a diccionario y agregar a la lista
        diccionario = json.loads(linea)
        mi_lista.append(diccionario)
        #print(linea)
        print("Se agregó especie: ",diccionario["nombre_co"])
        linea = archivo.readline()   #lee la siguiente línea
    archivo.close()  #no debe faltar
except FileNotFoundError:
    print("archivo no encontrado")
except UnicodeDecodeError:
    print("Formato no es legible")
##archivo = open('datos4.txt','r')
##lineas = archivo.readlines()
##print(lineas)
##archivo.close()

