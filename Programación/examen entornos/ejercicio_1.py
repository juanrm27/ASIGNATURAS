#EXAMEN JUAN REINA

def sumar(arg):
    total = 0
    if len(arg) == 0:
        return 0
    for val in arg:
        if val is int or val is float:
            total += val
        else:
            return 0
    return total

#Pruebas:
def si_no_pasan_argumentos_devuelve_cero():
    return sumar([])
     
def suma_lista_de_enteros_o_float():
    return sumar([2,2.5])
              
def no_falla_si_se_pasan_cadenas_devuelve_cero():
    return sumar(['h', 7])

def si_se_pasan_datos_complejos_devuelve_cero():
    return sumar([9+2j, 4])

def si_se_pasan_objetos_no_numericos_devuelve_cero():
    return sumar('')


print(si_no_pasan_argumentos_devuelve_cero)
print(suma_lista_de_enteros_o_float)
print(no_falla_si_se_pasan_cadenas_devuelve_cero)
print(si_se_pasan_datos_complejos_devuelve_cero)
print(si_se_pasan_objetos_no_numericos_devuelve_cero)
