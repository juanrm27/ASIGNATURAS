# def pedir():
#     fecha_nacimiento = {}

#     for i in range(1):
#         nombre = input('Nombre: ')
#         dia = input('Dia que naciste: ')
#         mes = input('Mes que naciste: ')
#         año = input('Año que naciste: ')
#         fecha_nacimiento[nombre] = {'dia':dia, 'mes':mes, 'año':año}

#     return fecha_nacimiento

# print(pedir())



def fecha_nacimiento():
    meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Noviembre','Diciembre']
    fecha = input('Dime cuando naciste (dd/mm/aaaa): ')
    partes = fecha.split('/')
    mes  = int(partes[1]) - 1
    mensaje = ' Naciste el dia ' + partes[0] + ' del mes ' + meses[mes] + ' del año ' + partes[2]
    return mensaje
    

print(fecha_nacimiento())

def fecha_nacimiento_2 ():
    meses = { 1:'Enero', 2:'Febrero', 3:'Marzo', 4:'Abril', 5:'Mayo', 6:'Junio', 7:'Julio',8:'Agosto',9:'Septiembre',10:'Octubre',11:'Noviembre', 12:'Diciembre' }
    fecha = input('Dime cuando naciste (dd/mm/aaaa): ')
    partes = fecha.split('/')
    mes  = int(partes[1]) - 1
    mensaje = ' Naciste el dia ' + partes[0] + ' del mes ' + meses[mes] + ' del año ' + partes[2]
    return mensaje

print(fecha_nacimiento_2())

