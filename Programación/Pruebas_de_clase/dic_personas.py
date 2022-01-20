

def introduce():
    personas = {}

    for i in range(1):
        nombre = input('Introduzca nombre: ')
        apellidos = input('Introduzca apellidos: ')
        dni = input('Introduzca DNI: ')
        personas[dni] = {'nombre':nombre, 'apellidos':apellidos}

    return personas 

print(introduce())