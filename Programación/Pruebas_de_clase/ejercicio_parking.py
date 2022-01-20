PRECIO_SEMANA = 100
PRECIO_DIA = 42
DIAS_SEMANA = 7

def calcular_coste(dias):

    # 1.- Calcular las semanas
    semanas = dias // DIAS_SEMANA
    # 2.- Calcular los dias restantes
    dias_restantes = dias % DIAS_SEMANA
    # 3.- Coste por precio semana
    coste_semanal = semanas * PRECIO_SEMANA
    # 4.- Coste por dias
    coste_dias = dias_restantes * PRECIO_DIA
    # 5.- Calculo del total
    total = coste_dias + coste_semanal

    return total



print(calcular_coste(35))


