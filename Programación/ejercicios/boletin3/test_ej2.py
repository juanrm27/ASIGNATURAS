import unittest
from ej2_canciones import Cancion, CD

class Test_cancion(unittest.TestCase):

    def test_existencia(self):
        prueba_cancion = Cancion()
        self.assertNotEqual(None,prueba_cancion)
    
    def test_constructor_parametros_correctos(self):
        prueba_cancion = Cancion('Viva', 'Paquito')
        self.assertEqual(prueba_cancion.autor, 'Paquito')
        self.assertEqual(prueba_cancion.nombre, 'Viva')
    
class Test_CD(unittest.TestCase):

    def test_existencia_CD(self):
        prueba_CD = CD()
        self.assertIsNotNone(prueba_CD)

    def test_lista_vacia(self):
        prueba_CD = CD()
        self.assertEqual(prueba_CD.lista_caciones, [])
        self.assertEqual(prueba_CD.contador, 0)
    
    def test_lista_vacia_agrega_cancion(self):
        prueba_CD = CD()
        prueba_cancion = Cancion('Viva', 'Paquito')
        prueba_CD.agrega_cancion(prueba_cancion)
        self.assertEqual(prueba_CD.contador, 1)
        self.assertEqual(prueba_CD.lista_caciones[0].nombre, 'Viva')
        self.assertEqual(prueba_CD.lista_caciones[0].autor, 'Paquito')
    
    def test_lista_vacia_elimina_cancion(self):
        prueba_cancion = Cancion('Viva', 'Paquito')
        prueba_CD = CD([prueba_cancion])
        prueba_CD.elimina_cancion(0)
        self.assertEqual(prueba_CD.contador, 0)
        self.assertEqual(prueba_CD.lista_caciones,[])
      