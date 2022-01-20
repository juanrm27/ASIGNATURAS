
class Persona: 
  def __init__(self, nombre, apellidos, edad, dni):
    self.nombre = nombre
    self.apellidos = apellidos
    self.edad = edad
    self.dni = dni

  def __str__(self):
    return "Persona: " + self.nombre + ' '+ self.apellidos + ' ' + self.edad + ' ' + self.dni

pers = Persona("Juan","Reina Muñiz", "18", "45712910X")
print(pers)