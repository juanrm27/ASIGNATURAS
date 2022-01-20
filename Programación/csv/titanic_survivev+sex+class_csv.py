import os
import csv
os.system('clear')
ruta = '/home/ubuntu/Desktop/ASIGNATURAS/Programación/csv/'

def leer_archivo():
    csv_in = open(ruta + 'titanic.csv')
    lector = csv.DictReader(csv_in)
    lista = list(lector)
    csv_in.close()
    return(lista)

supervivientes = 0
muertos = 0
mujeres = 0
hombres = 0
mujeres_vivas_clase1 = 0
mujeres_vivas_clase2 = 0

mujeres_muertas_clase1 = 0
mujeres_muertas_clase2 = 0

hombres_vivos_clase1 = 0
hombres_vivos_clase2 = 0

hombres_muertos_clase1 = 0
hombres_muertos_clase2 = 0


lista_titanic = leer_archivo()
for persona in lista_titanic:
    if persona['Survived'] == '1':
        if persona['Sex'] == 'male':
            if persona['Pclass'] == '1':
                supervivientes += 1
                mujeres += 1
                mujeres_vivas_clase1 += 1
            else:
                supervivientes += 1
                mujeres += 1
                mujeres_vivas_clase2+= 1
        else:
            if persona['Pclass'] == '1':
                supervivientes += 1
                hombres += 1
                hombres_vivos_clase1 += 1
            else:
                supervivientes += 1
                hombres += 1
                hombres_vivos_clase2+= 1
    else:
        if persona['Sex'] == 'female':
            if persona['Pclass'] == '1':
                muertos += 1
                mujeres += 1
                mujeres_muertas_clase1 += 1
            else:
                muertos += 1
                mujeres += 1
                mujeres_muertas_clase2 += 1
        else:
            if persona['Pclass'] == '1':
                muertos += 1
                hombres += 1
                hombres_muertos_clase1 += 1
            else:
                muertos += 1
                hombres += 1
                hombres_muertos_clase2+= 1
        


m_v_1= (mujeres_vivas_clase1)
m_m_1 = (mujeres_muertas_clase1)
m_v_2= (mujeres_vivas_clase2)
m_m_2 = (mujeres_muertas_clase2)
h_v_1 = (hombres_vivos_clase1)
h_m_1 = (hombres_muertos_clase1)
h_v_2 = (hombres_vivos_clase2)
h_m_2 = (hombres_muertos_clase2)

print('Mujeres vivas clase 1: ', (m_v_1))
print('Mujeres muertas clase 1: ', (m_m_1))
print('Mujeres vivas clase 2: ', (m_v_2))
print('Mujeres muertas clase 2: ', (m_m_2))


print('Hombres vivos clase 1: ', (h_v_1))
print('Hombres muertos clase 1: ', (h_m_1))
print('Hombres vivos clase 2: ', (h_v_2))
print('Hombres muertos clase 2: ', (h_m_2))
