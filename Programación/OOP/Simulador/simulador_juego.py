from random import randrange

def tablero_sencillo():
    ganador = 0
    tiradas = 0
    jug1 = 0
    jug2 = 0
    

    while not ganador:   
        tiradas += 1
        jug1 += randrange(1,6)
        jug2 += randrange(1,6)
        print(f'Tirada: {tiradas}\n  El Jugador 1 tiene: {jug1} puntos\n  El Jugador 2 tiene: {jug2} puntos')

        if jug1 >= 100:
            print(' ¡¡EL JUGADOR 1 HA GANADO!!')
            ganador = True
        elif jug2 >= 100:
            print(' ¡¡EL JUGADOR 2 HA GANADO!!')
            ganador = True

    return f'La partida ha terminado'

print(tablero_sencillo())