"""
Son funciones que admiten funciones como parámetros
y devuelven funciones
"""

def mi_decorador(funcion_a_decorar):
    def envoltura(*args,**kwagrs):
        print('------Empiezo a decorar')
        c = funcion_a_decorar(*args,**kwagrs)
        print(c)
        print('------Fin de la decoración')

    return envoltura


@mi_decorador
def saludar():
    print('HOLA MUNDO!!')

# resp = mi_decorador(saludar)
# resp()


@mi_decorador
def sumar(a,b):
    return a + b

# def restar(a,b):
#     return a - b

sumar(1,2)

