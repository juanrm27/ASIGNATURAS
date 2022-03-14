import unittest
from ejercicio1 import Persona

class TestPersona(unittest.TestCase):
    def test_clase_existe(self):
        persona = Persona()
        self.assertNotEqual(persona, None)
    
    def test_str_imprime_datos(self):
        p = Persona('Juan', 'Reina','54179201X')
        self.assertEqual(p.nombre,'Juan')
        self.assertEqual(p.apellido, 'Reina')
        self.assertEqual(p.dni, '54179201X')