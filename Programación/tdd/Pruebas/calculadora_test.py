import unittest
import calculadora

class CalculadoraTest(unittest.TestCase):
    def test_caracteres_no_numericos_devuelve_error(self):
        respuesta = calculadora.sumar('a,b')
        self.assertEqual(respuesta, "Error: Carácter no númerico")
    
    
def test_cadena_vacia_devuelve_cero(self):
    respuesta = calculadora.sumar('')
    self.assertEqual(respuesta,0)

# def un_numero_devuelve_el_numero():
#     return sumar('1')
# def un_caracter_devuelve_el_numero():
#     return sumar('a')

# def dos_numeros_devuelve_suma():
#     return sumar('2,3')

# def numeros_ilimitados_devuelve_suma():
#     return sumar('1,2,3,4')

# def numeros_separados_por_n():
#     return sumar('1n2n4n5,3')
        