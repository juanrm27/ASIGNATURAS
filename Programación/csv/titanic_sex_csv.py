import os
import csv

ruta = '/home/ubuntu/Desktop/ASIGNATURAS/Programación/csv/'

def leer_archivo():
    csv_in = open(ruta + 'titanic.csv')
    lector = csv.DictReader(csv_in)
    lista = list(lector)
    csv_in.close()
    return(lista)

supervivientes = 0
muertos = 0
mujeres_vivas = 0
hombres_vivos = 0
mujeres_muertas = 0
hombres_muertos = 0

lista_titanic = leer_archivo()
for persona in lista_titanic:
    if persona['Survived'] == '1':
        if persona['Sex'] == 'male':
            supervivientes += 1
            mujeres_vivas += 1
        else:
            supervivientes += 1
            hombres_vivos += 1
    else:
        if persona['Sex'] == 'female':
            muertos += 1
            mujeres_muertas += 1
        else:
            muertos += 1
            hombres_muertos += 1


m_v = (mujeres_vivas)
h_v = (hombres_vivos)
m_m = (mujeres_muertas)
h_m = (hombres_muertos)
print('Mujeres vivas: ', (m_v))
print('Hombres vivos: ', (h_v))
print('Mujeres muertas: ', (m_m))
print('Hombres muertos: ', (h_m))

