# import math
# class ejemplos():

#     @classmethod
#     def configurar(cls):
#         return 'Metodo de clase', cls
    
#     def suma(self, a, b):
#         return a+b

# e = ejemplos()
# print(e.suma(1,2))

# print(ejemplos.configurar())


class estudiante():
    def __init__(self,nombre,apellidos) -> None:
        self.__nombre = nombre
        self.__apellidos = apellidos

    def __str__(self) -> str:
        return f'Estudiante : {self.__nombre} {self.__apellidos}'

    @classmethod
    def estudiante_desde_json(cls,obj_json):
        estudiante = dict(obj_json) #{'nombre': 'Paco', 'apellidos': 'Lopez Garcia'}
        obj_estudiante = cls(estudiante['nombre'],estudiante['apellidos'])
        return obj_estudiante
    
    @classmethod
    def estudiante_desde_lista(cls, aboj_lista):
        obj_estudiante = cls
        return obj_estudiante

x = estudiante.estudiante_desde_json({'nombre': 'Paco', 'apellidos': 'Lopez Garcia'})
print(x)



