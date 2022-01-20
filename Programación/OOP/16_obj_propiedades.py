class Persona():
    def __init__(self,nombre, apellido, fecha_de_nacimiento) ->None:
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_de_nacimiento = fecha_de_nacimiento

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_fecha_de_nacimiento(self):
        return self.__fecha_de_nacimiento

