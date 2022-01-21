import unittest as ut
from num_18_metodos_estaticos import Calificaciones

class TestCalificaciones(ut.TestCase):
    def test_existencia(self):
        cal = Calificaciones()
        self.assertNotEqual(cal, None)
    
    def test_constructor_vacio_prpiedades_vacias(self):
        cal = Calificaciones()
        self.assertEqual(cal.nombre, '')
        self.assertEqual(cal.notas, [])
    
    def test_constructor_recibe_valores_establece_props(self):
        cal = Calificaciones(['Raul',9.2,5,4.5,7,9,1])
        self.assertEqual(cal.nombre, 'Raul')
        self.assertEqual(cal.notas, [9.2,5,4.5,7,9,1,])
    
    def test_metodo_str_devuelve_alumno_calificacion(self):
        cal = Calificaciones(['Raul',9.2,5,4.5,7,9,1])
        cadena = cal.__str__()
        self.assertEqual(cadena,'Alumno: Raul tiene la calificacion BIEN')
    
    def test_calcula_calificacion_vacio_devuelve_None(self):
        cal = Calificaciones()
        self.assertEqual(cal.calcula_calificacion(),None)
    
    def test_calcula_calificacion_no_vacio_devuelve_None(self):
        cal = Calificaciones(['Raul',9.2,5,4.5,7,9,1])
        self.assertEqual(cal.calcula_calificacion(),'BIEN')
        
        
        