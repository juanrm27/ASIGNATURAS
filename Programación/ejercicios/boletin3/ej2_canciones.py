class Cancion():
    def __init__(self, nombre = '', autor = '') -> None:
        self.nombre = nombre
        self.autor = autor 

class CD():
    def __init__(self, lista = []) -> None:
        self.__lista_caciones = lista
        self.contador = len(lista)

    def agrega_cancion(self, tema):
        self.lista_caciones.append(tema)
        self.contador = len(self.lista_caciones)

    def elimina_cancion(self, indice):
       self.lista_caciones.pop(indice)
       self.contador = len(self.lista_caciones)
    
    @property
    def numero_canciones(self):
        return self.contador
    
    @property
    def canciones(self):
        return self.__lista_caciones

    @canciones.setter
    def canciones(self,lista_canciones):
        self.__lista_caciones = lista_canciones
