from pprint import pprint
archivo = 'listas2.py'
listas = open(archivo)
lineas = listas.readlines()
for l in lineas:
    pprint(l)

