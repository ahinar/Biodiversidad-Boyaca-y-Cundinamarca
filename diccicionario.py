# dicc_especie={"id":1,"Tipo": "ave","nombre_co":"Chavarrí ", "nombre_ci":"Chauna chavaria","habitat":"Puerto Boyacá",
#               "Latitud":  5.803213,"Longitud":-74.486819,"altitud":200,
#               "imagen":"https://inaturalist-open-data.s3.amazonaws.com/photos/364451393/large.jpeg" }
# lista_especies=[]
# lista_especies.append(dicc_especie)
# #print(lista_especies)

# #buscar informacion
# import requests
# resp = requests.get("https://colombia.inaturalist.org/observations/206076366")
# print(resp)
# # print(resp.content)
# # print(resp.text)
# dicc_especie={"id":2, "Tipo": "planta","nombre_co":"Nigua ", "nombre_ci":"Disterigma empetrifolium", "habitat":"Duitama",
#               "Latitud": 5.858625,"Longitud":-73.059167,"altitud":2300,
#               "imagen":"https://static.inaturalist.org/photos/364991088/large.jpg" }
# lista_especies.append(dicc_especie)
# dicc_especie={"id":3, "Tipo": "Ave","nombre_co":"Esmeralda Colicorta", "nombre_ci":"Chlorostilbon poortmani", "habitat":"Gachantivá",
#               "Latitud":  5.742432,"Longitud":-73.520657,"altitud":2300,
#               "imagen":"https://inaturalist-open-data.s3.amazonaws.com/photos/364241173/large.jpeg" }

# lista_especies.append(dicc_especie)

# dicc_especie={"id":4, "Tipo": "Mamifero","nombre_co":"Venado de Cola Blanca", "nombre_ci":"Odocoileus virginianus", "habitat":"El Cocuy",
#               "Latitud":  6.386188,"Longitud":-72.346253,"altitud":3940,
#               "imagen":"https://inaturalist-open-data.s3.amazonaws.com/photos/357868067/large.jpg" }

# lista_especies.append(dicc_especie)
# #print(lista_especies)

import json
#el archivo debe estar en la misma carpeta que el programa
# archivo = open("C:/Users/Fercho/OneDrive/Programacion/talentoTech/Explorador/Biodiversidad-Boyaca-y-Cundinamarca/diccionario.txt", mode="r")
# #verificamos que el archivo se pueda leer
# print(archivo.readable())
# #inicializar lista diccionario
# lista_bio =[]
# #aseguramos que lee las lineas
# string_bio = archivo.readline()
# dicc_bio =json.loads(string_bio)
# # impresiones de prueba nombre comun y habitat
# print("Nombre Comun: ", dicc_bio.get("nombre_co"))
# print("Habitat: ", dicc_bio.get("habitat"))
# print("Latidtud: ", dicc_bio.get("latitud"))
# print("Longitud: ", dicc_bio.get("longitud"))
# lista_bio.append(dicc_bio)

# #leer los siguientes elementos
# string_bio = archivo.readline()
# dicc_bio =json.loads(string_bio)
# lista_bio.append(dicc_bio)

# string_bio = archivo.readline()
# dicc_bio =json.loads(string_bio)
# lista_bio.append(dicc_bio)

# string_bio = archivo.readline()
# dicc_bio =json.loads(string_bio)
# lista_bio.append(dicc_bio)


# #print(lista_bio)
# print(lista_bio[-1].get("nombre_ci"))
# archivo.close()

# # Crea el archivo objeto
# # Dar el nombre del archivo 
# archivo_objeto = open("diccionario.txt",mode="r",encoding="utf-8")

# # Hace un ciclo, desde que hayan líneas de texto
# for cadena in archivo_objeto:
#     print(cadena)

# # Cerrar el archivo
# archivo_objeto.close()

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
#Leer archivo JSON y armar diccionarios y meterlos en una tupla
import json
#armar diccionario con datos de dos especies
#diccionario1={"id":6,"tipo":"anfibio","nombre_co":"Rana Andina","nombre_ci":"Hypsiboas gladiator","habitat":"bosque nuboso","latitud":4.5233,"longitud":-72.333,"altitud":2045,"imagen":""}
#diccionario2={"id":7,"tipo":"ave","nombre_co":"colibrí paramuno","nombre_ci":"Aglaeactis cupripennis","habitat":"bosque nuboso","latitud":4.5233,"longitud":-72.333,"altitud":2045,"imagen":""}
#Pedir datos desde la consola hasta que se introduzca el Id 0
while True:
    id = int(input("Introduzca el id de la especie "))
    if id ==0:
        break
    #pedir el resto de los datos
    tipoEspecie= input ("Introducir Tipo de Especie ")
    nombre = input ("Introducir nombre de la especie ")
    cientifico = input("Introducir nombre de la especie: ")
    habi= input("Introduzca donde Vive ")
    lat=float(input("Indique Latitud ") )
    longi= float(input("Indique la longitud "))
    altura= int(input("Introduzca la altitud "))
    urlImagen= input("Introduzca la url de la imagen ")
    #armar el diccionario con los datos introducidos
    diccionario={"id":id,"tipo":tipoEspecie, "nombre_co":nombre,"nombre_ci":cientifico,
                 "habitat":habi, "latitud":lat, "longitud":longi, "altitud":altura, "imagen":urlImagen}
    try:
        archivo = open('ejemplodic3.json','a')
        cadena1 = json.dumps(diccionario)+"\n"       
        archivo.write(cadena1)  #escribe la primera cadena
        archivo.close()  #no debe faltar
    except FileNotFoundError:
        print("archivo no encontrado")
    except UnicodeDecodeError:
        print("Formato no es legible")
    except Exception:
        print("Hubo un error")
print("listo Cargue especies")