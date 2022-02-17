from genericpath import exists
from os import path
from claseAlumno import Alumno

class Aula():
    def __init__(self, nom, archivo) -> None:
        if self.__comprueba_archivo(archivo):
            self.__nombre_clase = nom
            self.__alumnos = []
            self.__carga_alumnos(archivo)
        else:
            raise FileNotFoundError('NO EXISTE EL ARCHIVO')

    def __comprueba_archivo(self, archivo):
        if path.exists(archivo):
            resp = True
        else:
            resp = False
        return resp
    
    def __carga_alumnos(self, archivo):
        listado = self.__lista_de_alumnos_desde_csv(archivo)
        for alum in listado:
            alumno = Alumno(alum)
            self.__alumnos.append(alumno)

    def __str__(self) -> str:
        salida = f'\nClase de {self.__nombre_clase} - Alumnos y notas:\n'
        for alum in self.__alumnos:
            salida += f'{alum.nom_alumno} - {alum.calificacion}\n'
        return salida


# ===============================================
curso = 'core'
archivo = 'C:\Users\jmrei\Desktop\ASIGNATURAS\Programación\ejercicios\Boletin3\alumno.csv'
clase = Aula(curso, archivo)
print(clase)