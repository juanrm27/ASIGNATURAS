from random import randrange

objetivo= randrange(100)
veces = 0

for i in range(10):
    veces+=1
    intento = int(input("introduce numero: "))
    if objetivo > intento:
        print("Es mayor")
    elif objetivo< intento:
        print("Es menor")
    else:
        print(f"has acertado en {veces} intentos")
        break
if veces > 9:
    print("has perdido.\n El numero era {objetivo}")

