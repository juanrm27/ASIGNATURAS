#EXAMEN JUAN REINA

import unittest
import ejercicio_1

class TestCodigo(unittest.TestCase):

    def si_no_pasan_argumentos_devuelve_cero(self):
        resp = ejercicio_1.sumar([])
        self.assertEqual(resp, 0)

    def suma_lista_de_enteros_o_float(self):
        resp = ejercicio_1.sumar([2,2.5])
        self.assertEqual(resp,4.5)
       
    def no_falla_si_se_pasan_cadenas_devuelve_cero(self):
        resp = ejercicio_1.sumar(['h', 7])
        self.assertEqual(resp, 0)

    def si_se_pasan_datos_complejos_devuelve_cero(self):
        resp = ejercicio_1.sumar([9+2j,1])
        self.assertEqual(resp, 0)

    def si_se_pasan_objetos_no_numericos_devuelve_cero(self):
        resp = ejercicio_1.sumar('')
        self.assertEqual(resp, 0)