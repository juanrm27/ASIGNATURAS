import unittest
from ejercicio2 import Cuenta

class TestCuenta(unittest.TestCase):
    
    def test_clase_existe(self):
        cuenta = Cuenta()
        self.assertNotEqual(cuenta, None)