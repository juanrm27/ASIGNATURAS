origen = [1,2,3,4,5,'jose','Alan','Fernando']
numeros = []
alumnos = []

for x in origen:
    if type(x) == str:
        alumnos.append(x)
    else:
        numeros.append(x)
        
print(origen)
print(alumnos)
print(numeros)
