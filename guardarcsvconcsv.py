import csv

datos = [
    ['Nombre', 'Edad'],
    ['Ana', 23],
    ['Luis', 34],
    ['Carlos', 45]
]

with open('archivo.csv', mode='w', newline='', encoding='utf-8') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerows(datos)