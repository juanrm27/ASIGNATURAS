class Estudiante():

    def __init__(self,nombre = " ", notas = 0, min_aprobado = 50) -> None:
        self.__nombre = nombre
        self.__notas = notas
        self.__min_aprobado = min_aprobado
    
    @property
    def nombre(self):
        return self.__nombre

    @property
    def notas(self):
        return self.__notas

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre
    
    
    @notas.setter
    def es_aprobado(self):
        if self.__notas >= self.__min_aprobado:
            return 'Aprobado'
        else:
            return 'Suspenso'

    def _str_(self):
        return (f'Nombre: {self.__nombre}, Calificación: {self.__notas}')


print(Estudiante('Antonio', 52))

