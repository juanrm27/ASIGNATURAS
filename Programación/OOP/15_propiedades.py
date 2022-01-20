# Decorador para comprobar si los parametros son enteros

def son_enteros(funcion):
    def envoltura(*args):
        for i in args:
            if not type(i) is int:
                raise Exception('Parámetros no enteros')
        return funcion(*args)
        #Hacer mas cosas
    return envoltura

# Multiplicación números enteros

@son_enteros
def multiplicación(a,b):
    return a*b


# resp = son_enteros(multiplicación)
# print(resp(2.'a'))

resp = multiplicación(2,7)
print(resp)