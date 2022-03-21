import unittest
from ejercicio4 import Estudiante

class TestEstudiante(unittest.TestCase):
    
    def test_clase_existe(self):
        estudiante = Estudiante()
        self.assertNotEqual(estudiante, None)
    
    def test_str_imprime_datos(self):
        e = Estudiante ('Antonio', 52)
        self.assertEqual(e.nombre,'Antonio')
        self.assertEqual(e.notas, 52)