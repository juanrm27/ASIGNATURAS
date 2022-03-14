class Persona():

    def __init__(self,nombre = " ", apellido = " ", dni = " "):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
    
    @property
    def nombre(self):
        return self.__nombre

    @property
    def apellido(self):
        return self.__apellido

    @property
    def dni(self):
        return self.__dni
    
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre

    
    @dni.setter
    def dni(self,dni):
        self.__dni = dni
      
    @apellido.setter
    def apellido(self,apellido):
        self.__apellido = apellido
    
    
    def __str__(self):
        return (f'Nombre:  {self.__nombre}, Apellido: {self.__apellido}, DNI: {self.__dni}')
