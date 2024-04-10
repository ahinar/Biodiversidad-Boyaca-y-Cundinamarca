dicc_especie={"id":1,"Tipo": "ave","nombre_co":"Chavarrí ", "nombre_ci":"Chauna chavaria","habitat":"Puerto Boyacá",
              "Latitud":  5.803213,"Longitud":-74.486819,"altitud":200,
              "imagen":"https://inaturalist-open-data.s3.amazonaws.com/photos/364451393/large.jpeg" }
lista_especies=[]
lista_especies.append(dicc_especie)
#print(lista_especies)

#buscar informacion
import requests
resp = requests.get("https://colombia.inaturalist.org/observations/206076366")
print(resp)
# print(resp.content)
# print(resp.text)
dicc_especie={"id":2, "Tipo": "planta","nombre_co":"Nigua ", "nombre_ci":"Disterigma empetrifolium", "habitat":"Duitama",
              "Latitud": 5.858625,"Longitud":-73.059167,"altitud":2300,
              "imagen":"https://static.inaturalist.org/photos/364991088/large.jpg" }
lista_especies.append(dicc_especie)
dicc_especie={"id":3, "Tipo": "Ave","nombre_co":"Esmeralda Colicorta", "nombre_ci":"Chlorostilbon poortmani", "habitat":"Gachantivá",
              "Latitud":  5.742432,"Longitud":-73.520657,"altitud":2300,
              "imagen":"https://inaturalist-open-data.s3.amazonaws.com/photos/364241173/large.jpeg" }

lista_especies.append(dicc_especie)

dicc_especie={"id":4, "Tipo": "Mamifero","nombre_co":"Venado de Cola Blanca", "nombre_ci":"Odocoileus virginianus", "habitat":"El Cocuy",
              "Latitud":  6.386188,"Longitud":-72.346253,"altitud":3940,
              "imagen":"https://inaturalist-open-data.s3.amazonaws.com/photos/357868067/large.jpg" }

lista_especies.append(dicc_especie)
#print(lista_especies)
archivo = open("C:/Users/Fercho/OneDrive/Programacion/talentoTech/Explorador/Biodiversidad-Boyaca-y-Cundinamarca/diccionario.txt", mode="r")

print(archivo.readable())
print(archivo.readline())
print(archivo.readline())
print(archivo.readline())
print(archivo.readline())
archivo.close()