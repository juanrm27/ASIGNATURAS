# Crear una clase Tiempo, con atributos hora, minuto y segundo, que pueda ser instanciada indicando: los tres
# atributos, sólo la hora y minuto, o sólo la hora.
# Crear además los métodos necesarios para modificar la hora en cualquier momento de forma manual.
# Mantenga la integridad de los datos en todo momento definiendo las variables como privadas.
# Crear las pruebas unitarias para asegurar el correcto funcionamiento de la clase.

class Tiempo():
    def __init__(self, hora='00', minutos='00', segundos='00') -> None:
        self.__hora = hora
        self.__minuto = minutos
        self.__segundo = segundos

    @property
    def hora(self):
        return self.__hora
    @hora.setter
    def hora(self, hora):
        self.__hora = hora  

    @property
    def minuto(self):
        return self.__minuto
    @minuto.setter
    def minuto(self, minutos):
        self.__minuto = minutos

    @property
    def segundo(self):
        return self.__segundo
    @segundo.setter
    def segundo(self,segundos):
        self.__segundo = segundos

    