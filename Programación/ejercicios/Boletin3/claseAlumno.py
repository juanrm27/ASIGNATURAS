class Alumno():
    def __init__(self,alumno_notas=[]) -> None:

        if alumno_notas:
            self.__nombre = alumno_notas[0]
            self.__notas = alumno_notas[1:]
            self.__calificacion = self.calcula_calificacion()
        else:
            self.__nombre = ''
            self.__notas = []
            self.__calificacion = ''
    
    def __str__(self) -> str:
        return f'Alumno: {self.__nombre} tiene la calificación {self.__calificacion}'

    def calcula_calificacion(self):
        calificacion = ''

        if self.notas:
            nota_media = sum(self.notas)/len(self.notas)
            if nota_media < 5:
                calificacion = 'SUSPENSO'
            elif nota_media < 7:
                calificacion = 'BIEN'
            elif nota_media < 9:
                calificacion = 'NOTABLE'
            else:
                calificacion = 'SOBRESALIENTE'
            
        else:
            calificacion = None
        
        return calificacion

    @property
    def alumno(self):
        return self.__nombre

    @alumno.setter
    def alumno(self,nuevo_alumno):
        self.__nombre = nuevo_alumno

    
    @property
    def notas(self):
        return self.__notas

    @notas.setter
    def notas(self, nuevas_notas):
        if self.valida_notas(nuevas_notas):
            self.__notas = nuevas_notas
            self.__calificacion = self.calcula_calificacion()
        else:
            raise Exception('Notas inválidas')
    
    @property
    def calificacion(self):
        return self.__calificacion

    @staticmethod
    def valida_notas(lista_notas):
        valido = True
        if lista_notas == []:
            valido = False

        for nota in lista_notas:
            if not type(nota) in (int,float) or not (0.0<= nota <= 10.0) :
                valido = False
        
        return valido