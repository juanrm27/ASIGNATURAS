class Cancion():
    def __init__(self, nombre = '', autor = '') -> None:
        self.nombre = nombre
        self.autor = autor 

class CD():
    def __init__(self, lista = []) -> None:
        self.lista_caciones = lista
        self.contador = len(lista)

    def agrega_cancion(self, tema):
        self.lista_caciones.append(tema)
        self.contador = len(self.lista_caciones)

    def elimina_cancion(self, indice):
       self.lista_caciones.pop(indice)
       self.contador = len(self.lista_caciones)
    