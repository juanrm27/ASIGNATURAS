# Crear una clase Coche, a través de la cual se pueda conocer el color del coche, la marca, el modelo, el número de puertas y la matrícula.
# Crear el constructor del coche, así como los métodos que considere necesarios.
# Crear las pruebas unitarias necesarias para comprobar que se pueden establecer y consultar los valores de los atributos.


class Coche():
    def __init__(self, color='', marca='', modelo='', numero_puertas='', matricula='') -> None:
        self.__color = color
        self.__marca = marca
        self.__modelo = modelo
        self.__numero_puertas = numero_puertas
        self.__matricula = matricula    
    
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color):
        self.__color = color  
    
    @property
    def marca(self):
        return self.__marca
    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @property
    def modelo(self):
        return self.__modelo
    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo  
    
    @property
    def numero_puertas(self):
        return self.__numero_puertas
    @numero_puertas.setter
    def numero_puertas(self, numero_puertas):
        self.__numero_puertas = numero_puertas  
    
    @property
    def matricula(self):
        return self.__matricula
    @matricula.setter
    def matricula(self,matricula):
        self.__matricula = matricula

    def __str__(self):
        return (f'Color: {self.__color}, Marca: {self.__marca}, Modelo: {self.__modelo}, Número de puertas: {self.__numero_puertas}, Matrícula: {self.__matricula}')


c1 = Coche('Rojo', 'Peugeot', '207', 4, '1750-GCH')
print(c1)
c2 = Coche('Azul','Toyoya','RAV4',4 ,'5032-ZRA')
print(c2)

