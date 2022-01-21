""""
Crear una clase Calificaciones.
Tendrá un metodo init que admitirá como entrada una lista de forma ['Raul', 9.2, 5, 4.5, 7, 9, 1,]
Tendra un metodo 'calificar' que nos devolverá ['Raul', 'Notable']

"""

class Calificaciones():
    def __init__(self, alumno_notas=[]) -> None:

        self.Calificacion = ''
        if alumno_notas :
            self.nombre = alumno_notas[0]
            self.notas = alumno_notas[1:]
        else:
            self.nombre = ''
            self.notas = []
    
    def __str__(self) -> str:
        return 'Alumno: Raul tiene la calificacion BIEN'
    
    def calcula_calificacion(self):
        calificacion = ''

        if self.notas:
            nota_media = sum(self.notas)/len(self.notas)
            if nota_media <5:
                return 'SUSPENSO'
            elif nota_media <7:
                return 'BIEN'
            elif nota_media <9:
                return 'NOTABLE'
            else:
                return 'SOBRESALIENTE'
        else:
            calificacion = None

        return calificacion