from os import confstr_names


def sumar(a,b):
    return a + b

def restar(a,b):
    return a - b

def calcular(operacion, a, b):
    # hacer cosas

    total = operacion(a,b)

    # hacer mas cosas
    return 'Hola'

print(calcular(restar,1,2))