import os
import settings

def clear():
    os.system('clear')

def buscar():
    """
    Busca en la carpeta seleccionada archivos que acaben en .py y la devuelve en una lista sin .py
    """
    lista_archivos = []
    archivo = os.scandir(settings.RUTA_BASE + settings.CODIGO)
    for a in archivo:
        if a.name.endswith('.py'):
            lista_archivos.append(a.name[:-3:])
    return lista_archivos

def agrupar(lista_archivos,miembros):
    """"
    Toma una lista de cadenas de texto y devuelve agrupamientos de esas cadenas
    """
    fila = ''
    for i in range(0,len(lista_archivos),miembros):
        temp = lista_archivos[i: i + miembros]
        fila += ','.join(temp) + '\n'
    return fila


def escribir(cadena,archivo):
    """
    Recoge la cadena de texto y la guarda en un archivo de texto
    """
    nuevo = open(archivo,'w')
    nuevo.write(cadena)
    nuevo.close()


ruta_salida = settings.RUTA_BASE + settings.CODIGO

clear()
x = buscar()
f = agrupar(x,5)
escribir(f,ruta_salida + '/funciones_lista.txt')
