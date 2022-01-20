persona = {}
def pers():
    for i in range(1):
        nombre = input('Inserte su nombre: ')
        apellidos = input('Inserte sus apellidos: ')
        edad = input('Inserte su edad: ')
        DNI = input('Inserte su DNI: ')
        persona= {'nombre':nombre, 'apellidos':apellidos, 'edad':edad, 'DNI':DNI}
    return persona 

print(pers())