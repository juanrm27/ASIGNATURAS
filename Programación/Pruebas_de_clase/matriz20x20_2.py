columnas = 20
filas = 20
matriz = []

for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(f"x")
    matriz.append(fila)

#---------------

for i in range(filas):
    linea = ''
    for j in range(columnas):
        linea += matriz [i][j]
    print(linea)

#deberes para mañana
M=[[1,2,3],
  [4,5,6],
  [7,8,9]]

H=[[9,8,7],
  [6,5,4],
  [3,2,1]]
