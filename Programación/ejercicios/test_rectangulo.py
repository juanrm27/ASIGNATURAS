import unittest
from ejercicios import rectangulo

class TestRectangulo(unittest.TestCase):

    def calcula_area(self):
        resp = rectangulo()
        self.assertEqual(resp, 0)