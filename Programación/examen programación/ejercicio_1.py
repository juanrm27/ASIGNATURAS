import os
import pprint

ruta = '/home/ubuntu/Desktop/ASIGNATURAS/Programación/Examen/'

with open(ruta + 'palabras.txt') as a:
    palabras = a.readlines()
    for linea in palabras:
       palabras.remove('e')
    print(linea)

