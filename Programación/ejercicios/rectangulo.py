# Crear una clase Rectángulo, con atributos base y altura.
# Crear también el constructor de la clase y los métodos necesarios para calcular el área y el perímetro.
# Crear las pruebas unitarias necesarias para asegurar que funciona correctamente.


class Rectangulo():
    def __init__(self, base=0, altura=0):
        self.__base = base
        self.__altura = altura
    def calcula_perimetro(self):
        return 2 * (self.__base + self.__altura)
    def calcula_area(self):
        return self.__base * self.__altura

    def __str__(self):
        return (f'Base =  {self.__base} y Altura = {self.__altura}')


rec_1 = Rectangulo(3,2)
print(rec_1)    

rec_2 = Rectangulo(4,3)
print(rec_2)

print(f'El area del rectángulo 1 es : {rec_1.calcula_area()}')
print(f'El perimetro del rectángulo 1 es: {rec_1.calcula_perimetro()}')   

print(f'El area del rectángulo 2 es : {rec_2.calcula_area()}')
print(f'El perimetro del rectángulo 2 es: {rec_2.calcula_perimetro()}')   
           

