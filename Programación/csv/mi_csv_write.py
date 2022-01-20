import csv
ruta = '/home/ubuntu/Desktop/ASIGNATURAS/Programación/csv/'

def csv_write():
    with open(ruta + 'nuevo_1.csv', 'a') as csv_write:
        escritor = csv.writer(csv_write)
        escritor.writerow(['jueves'] * 10 + ['viernes'])
        escritor.writerow(['Lo mejor de ambos mundos'] * 3)

csv_write()