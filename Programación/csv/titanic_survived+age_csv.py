import os
import csv

ruta = '/home/ubuntu/Desktop/ASIGNATURAS/Programación/csv/'

def leer_archivo():
    csv_in = open(ruta + 'titanic.csv')
    lector = csv.DictReader(csv_in)
    lista = list(lector)
    csv_in.close()
    return(lista)

# supervivientes = 0
# muertos = 0
# vivos_20_30_años = 0
# muertos_20_30_años = 0

# lista_titanic = leer_archivo()
# for persona in lista_titanic:
#     if persona['Survived'] == '1':      
#         if persona['Age'] >= '30':
#             supervivientes += 1
#             vivos_20_30_años += 1    
#         else:
#             if persona['Age'] <= '20':
#                 supervivientes += 1
#                 vivos_20_30_años += 1
#     else:
#         if persona['Age'] >= '30':
#             muertos += 1
#             muertos_20_30_años += 1    
#         else:
#             if persona['Age'] <= '20':
#                 muertos += 1
#                 muertos_20_30_años += 1

# print(muertos_20_30_años)
# print(vivos_20_30_años)



