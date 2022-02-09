#EXAMEN JUAN REINA

class Raton():
    __posicion_x = 0
    __posicion_y = 0
    __boton_izquierdo = 0
    __boton_derecho = 0

#Creamos los metodos getters y setters para su funcionamiento:
# Metodos= Getters: get , Setters: set

   #Get:
    def get_posicion_x(self):
        return self.__posicion_x
    def get_posicion_y(self):
        return self.__posicion_y
    def get_boton_izquierdo(self):
        return self.__boton_izquierdo
    def get_boton_derecho(self):
        return self.__boton_derecho
    #Set:    
    def set_posicion_x(self):
        return self.__posicion_x 
    def set_posicion_y(self):
        return self.__posicion_y 
    def set_boton_izquierdo(self):
        return self.__boton_izquierdo 
    def set_boton_derecho(self):
        return self.__boton_derecho 

#Especificamos los parametros de los metodos:
    def click(self):
        pass
    def doble_click(self):
        pass
    def mover(self):
        pass