def lee_fichero(nombre):
    try:
        f = open(nombre)
    except Exception as e:
        print(f'Error abriendo el archivo: {type(e).__name__}')
    else:
        datos = f.read()
        print(datos)
    
lee_fichero('hola.txt')

