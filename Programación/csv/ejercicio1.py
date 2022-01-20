# import pprint
# import os

# def clear():
#     os.system('clear')

# def datos_personales():
#     for i in range(1000):
#         Nombre = input('Nombre: ')
#         Apellido1 = input('Primer apellido: ')
#         Apellido2 = input('Segundo apellido: ')
#         Telefono = input('Numero de telefono: ')
#         Fecha_de_nacimiento = input('Fecha de nacimiento: (dd/mm/aaaa)')
#         Pregun = input('¿Desea cambiar sus respuestas?, si o no. Introduzca su respuesta :  ')

#         resultado = {'Nombre':Nombre,
#          'Primer apellido':Apellido1,
#          'Segundo apellido':Apellido2,
#          'Teléfono':Telefono,
#          'Fecha de nacimiento':Fecha_de_nacimiento}

#         if Pregun == str('no'):
#             pprint.pprint(resultado)
#             print('Que tenga un buen día :D')
#             break
#         else: 
#             pass
#         return resultado  

# clear()
# print(datos_personales())



from pprint import pprint
import os
import csv

def pedir_personas():
    seguir = True
    lista_personas = []

    while seguir:

        nombre = input('Nombre: ')
        apellido1 = input('Primer apellido: ')
        apellido2 = input('Segundo apellido: ')
        telefono = input('Numero de telefono: ')
        fecha_de_nacimiento = input('Fecha de nacimiento: (dd/mm/aaaa)')
        mi_dic = {'nombre':nombre, 'apellido1': apellido1, 'apellido2': apellido2, 'telefono': telefono, 'fecha_de_nacimiento': fecha_de_nacimiento}
        
        lista_personas.append(mi_dic)

        respuesta = input('¿Desea continuar s/n?')
        if respuesta.upper() == 'N':
            seguir = False
        os.system('clear')
    
    return lista_personas

def guardar_csv(contenido, destino):
    with open(destino, 'w',newline='') as f:
        escritor = csv.DictWriter(f,fieldnames =list(contenido[0].keys()))
        escritor.writeheader()
        escritor.writerows(contenido)



contenido = pedir_personas()       
ruta = '/home/ubuntu/Desktop/ASIGNATURAS/Programación/Ejercicios/personas.csv'

guardar_csv(contenido,ruta)